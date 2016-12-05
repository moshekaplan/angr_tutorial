# angr_tutorial
The goal is to demonstrate [angr](https://github.com/angr/angr)'s usage through a series of examples

1. Running angr
  1. https://github.com/angr/angr-doc/blob/master/examples/CSCI-4968-MBE/challenges/crackme0x00a/solve.py
  1. https://github.com/angr/angr-doc/blob/master/examples/CSCI-4968-MBE/challenges/crackme0x04/solve.py
1. Symbolizing cmd-line arguments
  1. See `args`
  2. [fairlight](https://github.com/angr/angr-doc/tree/master/examples/securityfest_fairlight)
1. Symbolizing a single integer
  1. See `magic_number`'s `symbolize_int()`
1. Symbolizing a single string
  1. See `bomb32/phase1`
1. Symbolizing function arguments
  1. Via modifying the stack contents directly
    1. See `bomb32/phase2`
    2. See https://github.com/angr/angr-doc/blob/master/examples/flareon2015_2/solve.py
  2. Via `stack_push(symbol)`
    1. See `magic_number`'s `symbolize_stack_param()`
1. Symbolizing user input
  1. read() (?? https://github.com/angr/angr-doc/blob/master/examples/fauxware/fauxware.c ??)
  2. scanf() (?? https://github.com/angr/angr-doc/blob/master/examples/defcon2016quals_baby-re_1/solve.py ??)
  3. gets()
  4. https://github.com/angr/angr-doc/blob/master/examples/csaw_wyvern/solve.py
1. Using success conditions not based on reaching an address
  1. Based on a specific register or memory values
  2. Based on user output (??? state.posix.dumps(1) ?? )
1. Finding multiple solutions
  1. https://github.com/angr/angr-doc/blob/master/examples/cmu_binary_bomb/solve.py#L85
1. Symbolizing files (?? https://docs.angr.io/docs/toplevel.html ??)
  1. https://github.com/angr/angr-doc/blob/master/examples/asisctffinals2015_license/solve.py
1. Using state constraints
  1. https://github.com/angr/angr-doc/blob/master/examples/google2016_unbreakable_0/solve.py
  2. https://github.com/angr/angr-doc/blob/master/examples/google2016_unbreakable_1/solve.py
  3. https://github.com/angr/angr-doc/blob/master/examples/asisctffinals2015_fake/solve.py
  4. https://github.com/angr/angr-doc/blob/master/examples/whitehatvn2015_re400/solve.py
1. Using callables
  1. https://github.com/angr/angr-doc/blob/master/docs/structured_data.md#callables
  2. https://github.com/angr/angr-doc/blob/master/examples/mma_howtouse/solve.py
1. Using hooks
  1. https://github.com/angr/angr-doc/blob/master/examples/ekopartyctf2015_rev100/solve.py
  2. https://github.com/angr/angr-doc/blob/master/examples/layer7_onlyone/solve.py
1. Finding exploitable conditions
  1. strcpy
    1. https://github.com/angr/angr-doc/blob/master/examples/strcpy_find/solve.py
