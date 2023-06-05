def pin(S):
    if S[0] == '0':
        return 'No'
    else:
        for i in range(1, 10):
            if S[i] != '0':
                return 'No'
        return 'Yes'
S = input()
print(pin(S))
