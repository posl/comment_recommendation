def isSplit(S):
    if S[0] == '0':
        return 'No'
    else:
        for i in range(len(S)):
            for j in range(len(S)):
                if i != j:
                    if S[i] == '1' and S[j] == '1':
                        if i < j:
                            for k in range(i+1, j):
                                if S[k] == '0':
                                    return 'Yes'
                        else:
                            for k in range(j+1, i):
                                if S[k] == '0':
                                    return 'Yes'
        return 'No'
S = input()
print(isSplit(S))
