def main():
    input = raw_input().rstrip().split()
    a = int(input[0])
    b = int(input[1])
    if a <= b:
        print 0
    else:
        print a - b * 2
