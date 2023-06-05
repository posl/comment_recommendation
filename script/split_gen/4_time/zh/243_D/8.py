def find_index(N, X, S):
    index = X
    for i in range(N):
        if S[i] == 'U':
            index = index // 2
        elif S[i] == 'L':
            index = index * 2 - 1
        else:
            index = index * 2 + 1
    return index
N, X = map(int, input().split())
S = input()
print(find_index(N, X, S))
