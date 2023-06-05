def main():
    N = int(input())
    P = list(map(int, input().split()))
    # 逆時針の転回回数を求める
    cnt = 0
    for i in range(N):
        if P[i] == i:
            cnt += 1
    if cnt == N:
        print(N)
    else:
        print(cnt + 2 * ((N - cnt) // 2))

if __name__ == '__main__':
    main()