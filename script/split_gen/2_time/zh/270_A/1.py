def main():
    input = raw_input()
    input = input.split()
    a = int(input[0])
    b = int(input[1])
    if a == 0 and b == 0:
        print 0
    elif a == 0:
        print b
    elif b == 0:
        print a
    else:
        print 7 - a - b
