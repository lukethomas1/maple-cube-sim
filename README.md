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

python3 maple-cube-sim.py -c 9999999 -p 15 -e SHOES
-----STAT HITS-----
% INT:
    15%: 1535226 hits, 15.352%
    20%: 180157 hits, 1.802%
    25%: 276514 hits, 2.765%
    30%: 130367 hits, 1.304%
    35%: 13182 hits, 0.132%
    40%: 11084 hits, 0.111%
    45%: 3314 hits, 0.033%
% STR:
    15%: 1535676 hits, 15.357%
    20%: 180071 hits, 1.801%
    25%: 276241 hits, 2.762%
    30%: 130569 hits, 1.306%
    35%: 13477 hits, 0.135%
    40%: 10929 hits, 0.109%
    45%: 3322 hits, 0.033%
% DEX:
    15%: 1532151 hits, 15.322%
    20%: 179994 hits, 1.800%
    25%: 275316 hits, 2.753%
    30%: 130342 hits, 1.303%
    35%: 13379 hits, 0.134%
    40%: 11151 hits, 0.112%
    45%: 3354 hits, 0.034%
% LUK:
    15%: 1536824 hits, 15.368%
    20%: 180215 hits, 1.802%
    25%: 275471 hits, 2.755%
    30%: 130200 hits, 1.302%
    35%: 13436 hits, 0.134%
    40%: 11096 hits, 0.111%
    45%: 3396 hits, 0.034%
% ALL STAT:
    15%: 29808 hits, 0.298%
    20%: 134564 hits, 1.346%
    25%: 1125 hits, 0.011%
    30%: 3488 hits, 0.035%
Total cubes used: 9999999
```
