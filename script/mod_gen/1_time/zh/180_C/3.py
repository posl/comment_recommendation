def main():
    import sys
    from math import sqrt
    N = int(sys.stdin.readline())
    ans = []
    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            ans.append(i)
            if i != N // i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()