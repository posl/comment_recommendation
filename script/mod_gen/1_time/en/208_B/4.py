def main():
    import sys
    import math
    input = sys.stdin.readline
    n = int(input())
    ans = 0
    for i in range(10, 0, -1):
        ans += n//math.factorial(i)
        n %= math.factorial(i)
    print(ans)

if __name__ == '__main__':
    main()