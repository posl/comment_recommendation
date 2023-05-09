def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    ans = 0
    for a in A:
        ans = 360 - (a + ans) % 360
    print(ans)

if __name__ == '__main__':
    main()