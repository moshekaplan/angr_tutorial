import angr
import claripy



FIND_ADDR = 0x0804849F
AVOID_ADDR = 0x080484A9
proj = angr.Project('args', load_options={'auto_load_libs':False})
arg1 = claripy.BVS('arg1', 10*8)
state = proj.factory.full_init_state(args=['./args', arg1])
path_group = proj.factory.path_group(state)
# Step until the explorer finds one of the addresses we are looking for or all paths are deadended
path_group.explore(find=FIND_ADDR, avoid=AVOID_ADDR)

solution_path = path_group.found[0]
solution_state = solution_path.state

print solution_state.se.any_str(arg1).rstrip(chr(0))
# Prints: +42*2¦¦3¦0
# Let's test:
# >> ./args +42*2
# >> echo $?
# 1
