def main():
    N = int(input())
    #約数の個数を数える
    count = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            count[j] += 1
    #奇数かつ約数が8個の数を数える
    ans = 0
    for i in range(1, N+1, 2):
        if count[i] == 8:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()