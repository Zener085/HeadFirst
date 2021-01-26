def double_tom(arg):
    print('Before: ' + arg)
    arg = arg * 2
    print('After: ' + arg)


def double_sarah(arg):
    print('Before: ' + arg)
    arg.append('More data')
    print('After:' + arg)


def prove():
    examples = [1, '1', [1, 2], True, 1.0]
    for x in examples:
        try:
            double_tom(x)
        except:
            print("Tom's program can't work with x = " + str(x))

    for x in examples:
        try:
            double_sarah(x)
        except:
            print("Sarah's program can't work with x = " + str(x))


prove()
