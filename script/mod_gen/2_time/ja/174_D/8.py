def main():
    N = int(input())
    S = input()
    # Rの個数
    cnt_R = S.count("R")
    # Rを左から数えてi番目の時、左側にあるWの個数
    cnt_W = [0] * (N+1)
    for i in range(N):
        cnt_W[i+1] = cnt_W[i] + (S[i] == "W")
    # Rを左から数えてi番目の時、右側にあるRの個数
    cnt_R2 = [0] * (N+1)
    for i in range(N):
        cnt_R2[N-i-1] = cnt_R2[N-i] + (S[N-i-1] == "R")
    # Rを左から数えてi番目の時、左側にあるWの個数 + 右側にあるRの個数
    cnt = [cnt_W[i] + cnt_R2[i] for i in range(N+1)]
    print(min(cnt))

if __name__ == '__main__':
    main()