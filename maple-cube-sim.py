import random
import sys
import argparse

import constants


def run_sim(stat_threshold: int, equip_type: str, cube_amount: int):
    """Simulate X cubes on a given equip type, printing out stat hits above a given threshold

    Args:
        stat_threshold (int): % stat threshold to print out at the end, ex. 30
        equip_type (str): Equip type to simulate, ex. SHOES (see keywords in constants.py)
        cube_amount (int): # of cubes to use, e.g 10000
    """

    # Pre-fill the dictionary to reduce time it takes for long runs
    stat_hits = {stat: {} for stat in constants.UNIQUE_LINE_VALUES.keys()}

    # Multiples of five between stat_threshold and 45 (including 45)
    for key in stat_hits.keys():
        for percent_val in range(stat_threshold, 46, 5):
            stat_hits[key][percent_val] = 0

    # Do simulation
    for _ in range(cube_amount):
        lines = simulate_random_three_lines(equip_type)
        values = simulate_stat_values(lines)
        stats = count_stats_from_lines(lines, values)

        for stat, value in stats.items():
            if value >= stat_threshold:
                stat_hits[stat][value] += 1

    # Print results
    print("---------------STAT HITS---------------")
    print(f"Equip Type: f{equip_type}")
    print(f"Total cubes used: {cube_amount:,}\n")
    for stat_name, percent_dict in stat_hits.items():
        print(f"{stat_name}:")
        for percent, count in sorted(percent_dict.items()):
            if count > 0:
                print(f"    {percent}%: {count} hits, {count/cube_amount:.5%}, 1 out of ~{cube_amount/count:,.0f} cubes")


def count_stats_from_lines(three_lines: (str,str,str), three_values: (int,int,int)) -> dict[str, int]:
    """Count stat totals of the given 3 lines & 3 values, return a dict of each stat with the % given by the potential

    Args:
        three_lines (str,str,str): The potential line description, ex. '% LUK'
        three_values (int,int,int): The value of each potential line, ex. '15'

    Returns:
        dict[str, int]: Dict of all five (incl. All Stat) stats to % stat given by potential, e.x '% LUK': 15
    """
    stat_counts = {key: 0 for key in constants.UNIQUE_LINE_VALUES.keys()}

    for i in range(len(three_lines)):
        if three_lines[i] == "% ALL STAT":
            # Add value of all stat line to every stat
            stat_counts = {stat: value + three_values[i] for stat, value in stat_counts.items()}
        elif three_lines[i] in stat_counts:
            stat_counts[three_lines[i]] += three_values[i]

    return stat_counts


def simulate_random_three_lines(equip_type: str) -> (str,str,str):
    """Generate 3 random potential line descriptions

    Args:
        equip_type (str): Equip type to generate lines for, ex. "SHOES"

    Returns:
        (str,str,str): Tuple with 3 string values representing the line description, ex. ('% LUK', "% HP", "% AVOID")
    """
    possibilities = constants.ALL_POSSIBLITIES + constants.EQUIP_POSSIBILITIES[equip_type]

    three_lines = []

    for _ in range(3):
        line = random.choice(possibilities)
        three_lines.append(line)

        # Can only get one instance of an equip-specific line
        if line in constants.EQUIP_POSSIBILITIES[equip_type]:
            possibilities.remove(line)
    return (*three_lines,)


def simulate_stat_values(three_lines: (str,str,str)) -> (int,int,int):
    """Generate values for the given potential lines. Use 0 as value for non-helpful lines.

    Args:
        three_lines (str,str,str): The three lines to generate values for, ex. ("% LUK", "% HP", "% AVOID")

    Returns:
        (int,int,int): Tuple with 3 int values corresponding to the given stat
    """
    three_values = []

    for i in range(len(three_lines)):
        line = three_lines[i]

        # If line is a stat line
        if line in constants.UNIQUE_LINE_VALUES:
            # If first pot line, always prime value
            if i == 0:
                value = constants.UNIQUE_LINE_VALUES[line][0]
                three_values.append(value)

            # If not first pot line, use non-prime value 90% of the time
            else:
                value = random.choices(constants.UNIQUE_LINE_VALUES[line], weights=[constants.CHANCE_OF_PRIME_LINE, 1 - constants.CHANCE_OF_PRIME_LINE])
                three_values.append(value[0])
        
        # Not a stat potential line, i.e. we do not care about the value
        else:
            three_values.append(0)

    return (*three_values,)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='python3 maple-cube-sim.py',
                    description='Simulate cube runs that reach a given stat threshold',
                    epilog='robot go burr')
    parser.add_argument('-c', '--count', type=int, help='Number of cubes to use')
    parser.add_argument('-p', '--percent', type=int, help='Percent threshold')
    parser.add_argument('-e', '--equip_type', type=str, help='Type of the equip')
    args = parser.parse_args()

    if not args.count or not args.percent or not args.equip_type:
        parser.print_help()
        # parser.print_usage() # for just the usage line
        parser.exit()
    run_sim(args.percent, args.equip_type, args.count)