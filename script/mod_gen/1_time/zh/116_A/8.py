def main():
    import sys
    line = sys.stdin.readline()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    s = (a * b) / 2
    print(int(s))

if __name__ == '__main__':
    main()