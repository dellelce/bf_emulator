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

    lang_dict = \
    {
        ",": "memory[ptr] = ord(input.pop(0))",
        ".": "output.append(chr(memory[ptr]))",
        ">": "ptr += 1",
        "<": "ptr -= 1",
        "+": "memory[ptr] = (memory[ptr] + 1) % 256",
        "-": "memory[ptr] = (memory[ptr] - 1) % 256",
        "[": "i = js[i - 1] if memoty[ptr] == 0 else i",
        "]": "i = js[i - 1] if memoty[ptr] != 0 else i",
    }

    ptr, i = 0, 0

    while i < len(code):
        cmd = code[i]

        act = lang_dict.get(cmd)

        if act is not None:
            exec(act)

        i += 1

    return "".join(output)
