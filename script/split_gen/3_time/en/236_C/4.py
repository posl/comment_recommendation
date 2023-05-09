def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    i = 0
    j = 0
    ans = []
    while i < N:
        if j < M and S[i] == T[j]:
            ans.append('Yes')
            j += 1
        else:
            ans.append('No')
        i += 1
    print('
'.join(ans))
