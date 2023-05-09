def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i, a in enumerate(A):
        if i + 1 == a:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()