def main():
    N, A, B = map(int, input().split())
    S = input()
    #print(N, A, B, S)
    #print(S[0], S[1], S[2], S[3], S[4], S[5], S[6], S[7])
    #回文でない文字列の数をカウント
    count = 0
    for i in range((N+1)//2):
        if S[i] != S[N-1-i]:
            count += 1
    #print(count)
    if count == 0:
        print(0)
    elif A < B:
        print(A*count)
    else:
        print(B*count)
