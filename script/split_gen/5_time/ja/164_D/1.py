def main():
    S = input()
    N = len(S)
    cnt = 0
    for i in range(N):
        for j in range(i, N):
            if int(S[i:j+1]) % 2019 == 0:
                cnt += 1
    print(cnt)
