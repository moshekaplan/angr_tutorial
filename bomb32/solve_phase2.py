def approach1():
    # Approach 1 - Replace the 6 integers with individual symbolized values
    import angr
    AFTER_READ_SIX_NUMBERS_ADDR = 0x8048B63
    FIND_ADDR = 0x8048B8E
    AVOID_ADDR = 0x8048B83

    proj = angr.Project('bomb', load_options={'auto_load_libs':False})
    state = proj.factory.blank_state(addr=AFTER_READ_SIX_NUMBERS_ADDR)

    # Create 6 symbolic integers and store them in memory
    six_int_offset = - 0x18
    sym_ints = []
    for i in range(6):
        sym_int = state.se.BVS("int_%d" % i, 8 * 4)
        state.memory.store(state.regs.ebp + six_int_offset + 4*i, sym_int, endness="Iend_LE")
        sym_ints.append(sym_int)

    path_group = proj.factory.path_group(state)
    path_group.explore(find=FIND_ADDR, avoid=AVOID_ADDR)
    solution_path = path_group.found[0]
    solution_state = solution_path.state

    for sym_int in sym_ints:
        print solution_state.se.any_int(sym_int)
    """
    Prints: 
    1
    2
    6
    24
    120
    720
    """

def approach2():
    # Approach 2 - Replace the 6 integers with a single symbolized array
    import angr
    AFTER_READ_SIX_NUMBERS_ADDR = 0x8048B63
    FIND_ADDR = 0x8048B8E
    AVOID_ADDR = 0x8048B83

    # Load the binary
    proj = angr.Project('bomb', load_options={'auto_load_libs':False})
    # Start right before the data comes in:
    state = proj.factory.blank_state(addr=AFTER_READ_SIX_NUMBERS_ADDR)


    six_int_offset = -0x18
    sym_int_array = state.se.BVS("int_arr", 8 * 4 * 6)
    state.memory.store(state.regs.ebp + six_int_offset, sym_int_array, endness="Iend_LE")

    path_group = proj.factory.path_group(state)
    path_group.explore(find=FIND_ADDR, avoid=AVOID_ADDR)
    solution_path = path_group.found[0]
    solution_state = solution_path.state

    # Examine EIP if we so desire
    print "EIP:", hex(solution_state.se.any_int(solution_state.regs.eip))

    # Print out the 6 integers in the array:
    for i in range(6):
        # Read 4 byte integers, fixing the endianess (since it's from memory)
        sym_int = solution_state.memory.load(state.regs.ebp + six_int_offset + i*4, 4, endness="Iend_LE")
        print solution_state.se.any_int(sym_int)
        
    """
    Prints: 
    1
    2
    6
    24
    120
    720
    """