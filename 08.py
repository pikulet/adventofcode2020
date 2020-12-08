def parse_inst(d):
    d = d.split()
    return [ d[0], int(d[1]) ]


with open('08-input', 'r') as f:
    data = f.read().splitlines()
    instructions = list(map(parse_inst, data))

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def execute(instructions, PRINT_LOOP):
    accumulator = 0
    remaining_inst = set(range(len(instructions)))

    index = 0
    while 0 <= index and index < len(instructions):
        if index not in remaining_inst:
            if PRINT_LOOP:
                print('Looping instruction encounted. Accumulator value:', accumulator)
            return

        remaining_inst.discard(index)

        inst = instructions[index]
        op_code = inst[0]

        if op_code == NOP:
            index += 1
            continue

        value = inst[1]

        if op_code == ACC:
            accumulator += value
            index += 1
            continue
        elif op_code == JMP:
            index += value
            continue
        else:
            break

    if index == len(instructions):
        print('Terminated with value:', accumulator)
        return accumulator

def swap_inst(index):
    global instructions
    op_code = instructions[index][0]
    if op_code == JMP:
        instructions[index][0] = NOP
    elif op_code == NOP:
        instructions[index][0] = JMP

execute(instructions, True)
for index in range(len(instructions)):
    if instructions[index] == ACC:
        continue

    swap_inst(index)
    execute(instructions, False)
    swap_inst(index)
