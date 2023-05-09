def main():
    from math import sqrt
    N = int(input())
    ans = []
    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            ans.append(i)
            if N // i != i:
                ans.append(N // i)
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()