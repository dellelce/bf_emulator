from collections import defaultdict


def jump_stack(code):
    stack = []
    jumps = {}

    for i, cmd in enumerate(code):
        if cmd == "[":
            stack.append(i)

        if cmd == "]":
            start = stack.pop(-1)
            jumps[start] = i
            jumps[i] = start

    return jumps


def brainfuck_emulator(code, input):
    code = list(code)
    input = list(input)

    output = []
    memory = defaultdict(int)
    js = jump_stack(code)

    ptr, i = 0, 0
    while i < len(code):
        cmd = code[i]

        # Input/Output
        if cmd == ",":
            memory[ptr] = ord(input.pop(0))
        if cmd == ".":
            output.append(chr(memory[ptr]))

        # Move pointer
        if cmd == ">":
            ptr += 1
        if cmd == "<":
            ptr -= 1

        # Incr/Decr memory
        if cmd == "+":
            memory[ptr] = (memory[ptr] + 1) % 256
        if cmd == "-":
            memory[ptr] = (memory[ptr] - 1) % 256

        # Loops
        if cmd == "[":
            if memory[ptr] == 0:
                i = js[i]

        if cmd == "]":
            if memory[ptr] != 0:
                i = js[i]

        i += 1

    return "".join(output)
