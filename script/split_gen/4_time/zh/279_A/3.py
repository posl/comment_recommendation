def count_underscores(S):
    count = 0
    for i in range(0, len(S)-1):
        if S[i] == 'v' and S[i+1] == 'w':
            count += 1
    return count
S = input()
print(count_underscores(S))
