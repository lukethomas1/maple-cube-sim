
import helpers

"""
https://kaizenms.net/?base=main&page=guide#itempotential
"""
CHANCE_TO_DROP_WITH_POT = 0.2
CHANCE_TO_DROP_AS_RARE = 0.9
CHANCE_TO_DROP_AS_EPIC = 0.09
CHANCE_TO_DROP_AS_UNIQUE = 0.01
CHANCE_TO_DROP_WITH_ONE_LINE = 0.9
CHANCE_TO_DROP_WITH_TWO_LINES = 0.09
CHANCE_TO_DROP_WITH_THREE_LINES = 0.01
CHANCE_TO_UPGRADE_POT = 0.05
CHANCE_TO_INCREASE_LINES = 0.05
"""
First line is always prime, second and third have 90% chance to be lower
"""
CHANCE_OF_PRIME_LINE = 0.1
"""
Certain potentials only show on specific equips.
For example, only weapons can get Watk%, damage to boss%, total damage%, etc.
Gloves can get Decent Sharp Eyes, etc. (Can only get these lines 1 time per item)

Disabled potentials: Watk% on Kataras. Matk% on weapons.
"""

ALL_POSSIBLITIES = [
    "% LUK",
    "% DEX",
    "% STR",
    "% INT",
    "% ALL STAT",
    "% HP",
    "% MP",
    "% AVOID",
    "% ACCURACY",
    "% WEAPON DEF",
    "% MAGIC DEF",
]

POTENTIAL_POSSIBILITIES = {
    "HAT": [

    ],
    "FACE": [

    ],
    "EYES": [

    ],
    "EARRINGS": [

    ],
    "SHOULDER": [

    ],
    "CAPE": [

    ],
    "OVERALL": [

    ],
    "PENDANT": [

    ],
    "WEAPON": [

    ],
    "OFFHAND": [

    ],
    "GLOVES": [

    ],
    "BELT": [

    ],
    "RING": [

    ],
    "SHOES": [
        "% CHANCE TO IGNORE DMG",
        "SKILL: HASTE",
    ]
}

# Prime line is first value, non-prime second value
UNIQUE_LINE_VALUES = {
    "% LUK": [15, 10],
    "% DEX": [15, 10],
    "% STR": [15, 10],
    "% INT": [15, 10],
    "% ALL STAT": [10, 5],
}