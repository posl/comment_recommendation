def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = 0
        for a in A:
            if a % 2 == 1:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()