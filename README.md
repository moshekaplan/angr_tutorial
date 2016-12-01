# angr_tutorial
The goal is to demonstrate [angr](https://github.com/angr/angr)'s use through a series of examples

1. Symbolizing cmd-line arguments (args)
2. Symbolizing a single integer (magic_number)
2. Symbolizing a single string (bomb32/phase1)
3. Symbolizing function arguments
    1. via modifying the stack contents directly (bomb32/phase2)
    2. via s.stack_push(symbol)
4. Symbolizing user input (???)
  1. sscanf()
  2. gets()
5. Examining user output (??? state.posix.dumps(1) )
