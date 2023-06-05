def count_bottoms(S):
    count = 0
    for i in range(len(S)):
        if S[i] == 'w':
            count += S.count('v', i + 1)
    return count
S = input()
print(count_bottoms(S))
