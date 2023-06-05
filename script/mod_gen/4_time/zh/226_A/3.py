def main():
    import sys
    import math
    for line in sys.stdin:
        x = float(line)
        print(int(math.floor(x + 0.5)))

if __name__ == '__main__':
    main()