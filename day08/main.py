full_instructions = open('input').read().split('\n')[:-1]

test_instructions = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]


def execute(instructions):
    position = 0
    position_history = []
    accumulator = 0

    while position not in position_history:
        position_history.append(position)
        cur_ins = instructions[position].split(' ')
        com = cur_ins[0]
        amount = int(cur_ins[1])
        if com == 'nop':
            position += 1
        if com == 'acc':
            accumulator += amount
            position += 1
        if com == 'jmp':
            position += amount
        if position >= len(instructions):
            return accumulator
    return accumulator


def validate_execution(instructions):
    position = 0
    position_history = []
    accumulator = 0

    while position not in position_history:
        position_history.append(position)
        cur_ins = instructions[position].split(' ')
        com = cur_ins[0]
        amount = int(cur_ins[1])
        if com == 'nop':
            position += 1
        if com == 'acc':
            accumulator += amount
            position += 1
        if com == 'jmp':
            position += amount
        if position >= len(instructions):
            return True
    return False


def validate_instuctions(instructions):
    for ins_num in list(range(len(instructions))):
        com = instructions[ins_num]
        if com[0:3] == 'nop':
            instructions[ins_num] = 'jmp' + com[3:]
        elif com[0:3] == 'jmp':
            instructions[ins_num] = 'nop' + com[3:]
        else:
            continue
        if validate_execution(instructions):
            return instructions
        instructions[ins_num] = com


def find_correct_answer(instructions):
    instructions = validate_instuctions(instructions)
    return execute(instructions)


print(f'Part one: {execute(full_instructions)}')


print(f'Part two: {find_correct_answer(full_instructions)}')
