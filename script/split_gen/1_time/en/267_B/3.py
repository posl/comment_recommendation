def isSplit(S):
    if S[0] == '0':
        return 'No'
    else:
        for i in range(1, 10):
            for j in range(i+1, 10):
                if S[i] == '1' and S[j] == '1':
                    if S[i+1:j] == '0' * (j-i-1):
                        return 'Yes'
        return 'No'
