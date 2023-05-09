def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        while a % 2 == 0 or a % 3 == 0:
            if a % 2 == 0:
                a //= 2
                ans += 1
            elif a % 3 == 0:
                a //= 3
                ans += 1
    for a in A:
        if a != A[0]:
            ans = -1
            break
    print(ans)

if __name__ == '__main__':
    main()