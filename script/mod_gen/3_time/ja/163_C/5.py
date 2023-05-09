def main():
    N = int(input())
    A = list(map(int, input().split()))
    #部下の数を数える
    sub = [0] * N
    for i in range(N - 1):
        sub[A[i] - 1] += 1
    #部下の数を出力
    for i in range(N):
        print(sub[i])

if __name__ == '__main__':
    main()