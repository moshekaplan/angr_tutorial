# angr_tutorial
The goal is to demonstrate [angr](https://github.com/angr/angr)'s usage through a series of examples

1. Symbolizing cmd-line arguments (See `args`, [fairlight](https://github.com/angr/angr-doc/tree/master/examples/securityfest_fairlight))
2. Symbolizing a single integer (See `magic_number`'s `symbolize_int()` )
2. Symbolizing a single string (See `bomb32/phase1`)
3. Symbolizing function arguments
    1. via modifying the stack contents directly (See `bomb32/phase2`)
    2. via `stack_push(symbol)` (See `magic_number`'s `symbolize_stack_param()`)
4. Symbolizing user input
  1. read() (?? https://github.com/angr/angr-doc/blob/master/examples/fauxware/fauxware.c ??)
  2. scanf() (?? https://github.com/angr/angr-doc/blob/master/examples/defcon2016quals_baby-re_1/solve.py ??)
  3. gets()
5. Using alternate success conditions
  1. Based on a specific register or memory values
  2. Based on user output (??? state.posix.dumps(1) ?? )
6. Symbolizing files (?? https://docs.angr.io/docs/toplevel.html ??)
  1. https://github.com/angr/angr-doc/blob/master/examples/asisctffinals2015_license/solve.py
7. Using state constraints
  1. https://github.com/angr/angr-doc/blob/master/examples/google2016_unbreakable_0/solve.py
  2. https://github.com/angr/angr-doc/blob/master/examples/google2016_unbreakable_1/solve.py
  3. https://github.com/angr/angr-doc/blob/master/examples/asisctffinals2015_fake/solve.py
  4. https://github.com/angr/angr-doc/blob/master/examples/whitehatvn2015_re400/solve.py
8. Using hooks
  1. https://github.com/angr/angr-doc/blob/master/examples/ekopartyctf2015_rev100/solve.py
