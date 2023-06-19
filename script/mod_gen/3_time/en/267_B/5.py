def isSplit(S):
    if S[0] == '0':
        return 'No'
    else:
        for i in range(1, 10):
            if S[i] == '1' and S[i-1] == '0':
                for j in range(i+1, 10):
                    if S[j] == '1' and S[j-1] == '0':
                        for k in range(i, j):
                            if S[k] == '0':
                                return 'Yes'
        return 'No'
S = input()
print(isSplit(S))
