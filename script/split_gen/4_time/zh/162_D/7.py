def main():
    N = int(input())
    S = input()
    R = 0
    G = 0
    B = 0
    for i in range(N):
        if S[i] == 'R':
            R += 1
        elif S[i] == 'G':
            G += 1
        else:
            B += 1
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            k = 2 * j - i
            if k < N:
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
                    cnt += 1
    print(R*G*B - cnt)
