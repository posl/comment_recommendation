def isSplit(S):
    if S[0] == '0':
        return 'No'
    for i in range(1, 10):
        if S[i] == '1':
            for j in range(i+1, 10):
                if S[j] == '1':
                    for k in range(i+1, j):
                        if S[k] == '0':
                            return 'Yes'
    return 'No'
S = input()
print(isSplit(S))
