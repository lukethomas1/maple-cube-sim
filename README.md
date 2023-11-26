# maple-cube-sim
Cube simulator for Maplestory (KaizenMS v92)

Note: Currently only has the possible item-specific potential lines for shoes, need to fill in the other equip types in ```constants.py```.

```
usage: python3 maple-cube-sim.py [-h] [-c COUNT] [-p PERCENT] [-e EQUIP_TYPE]

Simulate cube runs that reach a given stat threshold

options:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Number of cubes to use
  -p PERCENT, --percent PERCENT
                        Percent threshold
  -e EQUIP_TYPE, --equip_type EQUIP_TYPE
                        Type of the equip
```

```
Example usage:

python3 maple-cube-sim.py -c 99999999 -p 15 -e SHOES
Stat threshold: 15
Equip Type: SHOES
Cube amount: 99,999,999
Running simulation...

---------------STAT HITS---------------
% LUK:
    15%: 8456032 hits, 8.45603%, 1 out of ~12 cubes
    20%: 2563104 hits, 2.56310%, 1 out of ~39 cubes
    25%: 1331777 hits, 1.33178%, 1 out of ~75 cubes
    30%: 241710 hits, 0.24171%, 1 out of ~414 cubes
    35%: 62858 hits, 0.06286%, 1 out of ~1,591 cubes
    40%: 9504 hits, 0.00950%, 1 out of ~10,522 cubes
    45%: 451 hits, 0.00045%, 1 out of ~221,729 cubes
% DEX:
    15%: 8455009 hits, 8.45501%, 1 out of ~12 cubes
    20%: 2562426 hits, 2.56243%, 1 out of ~39 cubes
    25%: 1330206 hits, 1.33021%, 1 out of ~75 cubes
    30%: 242668 hits, 0.24267%, 1 out of ~412 cubes
    35%: 62675 hits, 0.06268%, 1 out of ~1,596 cubes
    40%: 9615 hits, 0.00962%, 1 out of ~10,400 cubes
    45%: 472 hits, 0.00047%, 1 out of ~211,864 cubes
% STR:
    15%: 8455162 hits, 8.45516%, 1 out of ~12 cubes
    20%: 2562645 hits, 2.56265%, 1 out of ~39 cubes
    25%: 1330419 hits, 1.33042%, 1 out of ~75 cubes
    30%: 241894 hits, 0.24189%, 1 out of ~413 cubes
    35%: 62690 hits, 0.06269%, 1 out of ~1,595 cubes
    40%: 9542 hits, 0.00954%, 1 out of ~10,480 cubes
    45%: 448 hits, 0.00045%, 1 out of ~223,214 cubes
% INT:
    15%: 8454791 hits, 8.45479%, 1 out of ~12 cubes
    20%: 2561199 hits, 2.56120%, 1 out of ~39 cubes
    25%: 1331194 hits, 1.33119%, 1 out of ~75 cubes
    30%: 241836 hits, 0.24184%, 1 out of ~414 cubes
    35%: 63209 hits, 0.06321%, 1 out of ~1,582 cubes
    40%: 9498 hits, 0.00950%, 1 out of ~10,529 cubes
    45%: 434 hits, 0.00043%, 1 out of ~230,415 cubes
% ALL STAT:
    15%: 1093319 hits, 1.09332%, 1 out of ~91 cubes
    20%: 152051 hits, 0.15205%, 1 out of ~658 cubes
    25%: 8092 hits, 0.00809%, 1 out of ~12,358 cubes
    30%: 408 hits, 0.00041%, 1 out of ~245,098 cubes
```

Full list of equip types (not case-sensitive):
```
HAT
FACE
EYES
EARRINGS
SHOULDER
CAPE
OVERALL
PENDANT
WEAPON
OFFHAND
GLOVES
BELT
RING
SHOES
```
Note: Only shoes implemented so far, need help filling out EQUIP_POSSIBILITIES in constants.py