def main():
    import sys
    import math
    N = int(input())
    if N < 1 or N > 300:
        sys.exit()
    else:
        result = math.floor(1.08 * N)
        if result < 206:
            print("Yay!")
        elif result == 206:
            print("so-so")
        else:
            print(":(")

if __name__ == '__main__':
    main()