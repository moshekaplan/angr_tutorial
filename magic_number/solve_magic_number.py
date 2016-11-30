import angr

# This is the address right after the call to atoi()
BEFORE_IS_MAGICAL_CALL_ADDR = 0x080484B9
FIND_ADDR = 0x080484CE
AVOID_ADDR = 0x080484E0

# Load the binary
proj = angr.Project('magic_number', load_options={'auto_load_libs':False})
# Start right before the data comes in:
state = proj.factory.blank_state(addr=BEFORE_IS_MAGICAL_CALL_ADDR)

# Approach 1 - create a symbolic value for eax.
number = state.se.BVS("number", 8 * 4)
state.regs.eax = number
# Create a path group 
path_group = proj.factory.path_group(state)
# Step until the explorer finds one of the addresses we are looking for or all paths are deadended
path_group.explore(find=FIND_ADDR, avoid=AVOID_ADDR)

solution_path = path_group.found[0]
solution_state = solution_path.state

print solution_state.se.any_int(number)
# prints 874742785
"""
(venv) ./magic_number 874742785
Your number is magical!
"""
