def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = sum(A)
    if ans < 0:
        ans = -ans
    if N % 2 == 0:
        ans = ans * 2
    print(ans)

if __name__ == '__main__':
    main()