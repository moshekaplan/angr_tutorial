import angr

BEFORE_STRINGS_NOT_EQUAL_ADDR = 0x8048B2C
FIND_ADDR = 0x8048B43
AVOID_ADDR = 0x8048B3

# Load the binary
proj = angr.Project('bomb', load_options={'auto_load_libs':False})
# Start right before the data comes in:
state = proj.factory.blank_state(addr=BEFORE_STRINGS_NOT_EQUAL_ADDR)

# Approach 1 - create an input string, and put a reference to it in eax.
# a symbolic input string with a length up to 32 bytes
input_string = state.se.BVS("input_string", 8 * 32)
HARDCODED_ADDRESS = 0xd0000010
state.memory.store(HARDCODED_ADDRESS, input_string)
state.regs.eax = HARDCODED_ADDRESS

# Create a path group 
path_group = proj.factory.path_group(state)
# Step until the explorer finds one of the addresses we are looking for or all paths are deadended
path_group.explore(find=FIND_ADDR, avoid=AVOID_ADDR)

solution_path = path_group.found[0]
solution_state = solution_path.state

print solution_state.se.any_str(input_string).rstrip(chr(0))
# Prints: 'Public speaking is very easy.'