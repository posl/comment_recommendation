def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for a in A:
        if a < 0:
            cnt += 1
            a = -a
        ans += a
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - min(A) * 2)

if __name__ == '__main__':
    main()