"""
Inspired from real-world Brainf**k, we want to create an interpreter of that
language which will support the following instructions (the machine memory or
"data" should behave like a potentially infinite array of bytes, initialized to
0):

> increment the data pointer (to point to the next cell to the right).
< decrement the data pointer (to point to the next cell to the left).
+ increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
- decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
. output the byte at the data pointer.
, accept one byte of input, storing its value in the byte at the data pointer.
[ if the byte at the data pointer is zero, then instead of moving the
  instruction pointer forward to the next command, jump it forward to the command
  after the matching ] command.
] if the byte at the data pointer is nonzero, then instead of moving the
  instruction pointer forward to the next command, jump it back to the command
  after the matching [ command.

The function will take in input...

the program code, a string with the sequence of machine instructions,
the program input, a string, eventually empty, that will be interpreted as an
array of bytes using each character"s ASCII code and will be consumed by the ,
instruction

... and will return ...

the output of the interpreted code (always as a string), produced by the . instruction.
"""
import brainfuck


def assert_equal(left, right):
    try:
        assert left == right
    except AssertionError:
        raise AssertionError("{} != {}".format(left, right))


def test_all():
    assert_equal(brainfuck.brainfuck_emulator(",-.", "\x00"), "\xff")
    assert_equal(brainfuck.brainfuck_emulator(",+.", "\xff"), "\x00")
    assert_equal(brainfuck.brainfuck_emulator(",-.,+.,-.,-.,-.,-.,-.,-.,+.,-.,-.,-.", 'Idmmp!Xpqme"'), "Hello World!")
    assert_equal(brainfuck.brainfuck_emulator(",-.,+.,-..+++.,-.,-.,-.,+.,-.,-.,-.", 'Idm!Xpqme"'), "Hello World!")
    assert_equal(
        brainfuck.brainfuck_emulator(",-.>,+.,-.<>.>+++.,-.,-.,-.,+.,-.,-.,-.", 'Idm!Xpqme"'),
        "Hell\x03 World!",
    )
    assert_equal(brainfuck.brainfuck_emulator(",<,<,<,.>.>.>.", "ABCD"), "DCBA")
    assert_equal(brainfuck.brainfuck_emulator(",+[-.,+]", "f948p9jhezvg\xff"), "f948p9jhezvg")
    assert_equal(brainfuck.brainfuck_emulator(",[.[-],]", "namfybcy1rfm\x00"), "namfybcy1rfm")
    assert_equal(
        brainfuck.brainfuck_emulator("+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.", " "),
        "hello world",
    )
    assert_equal(brainfuck.brainfuck_emulator(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.", chr(8) + chr(9)), chr(72))
    assert_equal(
        brainfuck.brainfuck_emulator(
            ",>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]",  # noqa
            "\n",
        ),
        "1, 1, 2, 3, 5, 8, 13, 21, 34, 55",
    )
