import random
import sys
import argparse

import constants

def run_sim(stat_threshold, equip_type, run_amount):

    stat_hits = {}

    for cube_index in range(run_amount):
        lines = simulate_random_three_lines(equip_type)
        values = simulate_stat_values(lines)
        stats = count_stats_from_lines(lines, values)

        for stat, value in stats.items():
            if value >= stat_threshold:
                if stat not in stat_hits:
                    stat_hits[stat] = {}
                if value not in stat_hits[stat]:
                    stat_hits[stat][value] = 1
                else:
                    stat_hits[stat][value] += 1

    print("-----STAT HITS-----")
    for stat_name, percent_dict in stat_hits.items():
        print(f"{stat_name}:")
        for percent, count in sorted(percent_dict.items()):
            print(f"    {percent}%: {count} hits, {count/run_amount:.3%}")
    print(f"Total cubes used: {run_amount}")

def count_stats_from_lines(three_lines: (str,str,str), three_values: (int,int,int)) -> dict[str, int]:
    stat_counts = {key: 0 for key in constants.UNIQUE_LINE_VALUES.keys()}

    for i in range(len(three_lines)):
        if three_lines[i] == "% ALL STAT":
            stat_counts = {stat: value + three_values[i] for stat, value in stat_counts.items()}
        elif three_lines[i] in stat_counts:
            stat_counts[three_lines[i]] += three_values[i]

    return stat_counts

def simulate_random_three_lines(equip_type: str) -> (str,str,str):
    """asdf

    Args:
        equip_type (str): ex. "SHOES"
    """
    possibilities = constants.ALL_POSSIBLITIES + constants.POTENTIAL_POSSIBILITIES[equip_type]

    three_lines = []

    for _ in range(3):
        line = random.choice(possibilities)
        three_lines.append(line)

        # Can only get one instance of an equip-specific line
        if line in constants.POTENTIAL_POSSIBILITIES[equip_type]:
            possibilities.remove(line)
    return (*three_lines,)

def simulate_stat_values(three_lines: (str,str,str)) -> (int,int,int):
    three_values = []

    for line in three_lines:
        if line in constants.UNIQUE_LINE_VALUES:
            value = random.choices(constants.UNIQUE_LINE_VALUES[line], weights=[1 - constants.CHANCE_OF_PRIME_LINE, constants.CHANCE_OF_PRIME_LINE])
            three_values.append(value[0])
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