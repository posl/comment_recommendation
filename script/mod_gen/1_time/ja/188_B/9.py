def main():
    N = int(input()) # Nを入力
    A = list(map(int, input().split())) # Aを入力
    B = list(map(int, input().split())) # Bを入力
    ans = 0
    for i in range(N):
        ans += A[i] * B[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()