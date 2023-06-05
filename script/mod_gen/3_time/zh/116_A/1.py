def main():
    import sys
    import math
    line = sys.stdin.readline()
    line = line.split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(int(area))

if __name__ == '__main__':
    main()