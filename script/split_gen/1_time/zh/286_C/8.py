def main():
    N,A,B = map(int,input().split())
    S = input()
    S_r = S[::-1]
    count = 0
    for i in range(N//2):
        if S[i] != S_r[i]:
            if S[i] == 'a':
                count += A
                S = S[:i] + 'a' + S[i+1:]
            elif S_r[i] == 'a':
                count += A
                S = S[:N-i-1] + 'a' + S[N-i:]
            else:
                count += B
                S = S[:i] + 'a' + S[i+1:]
                S = S[:N-i-1] + 'a' + S[N-i:]
    if N % 2 == 1:
        if S[N//2] == 'a':
            count += A
        else:
            count += B
    print(count)
