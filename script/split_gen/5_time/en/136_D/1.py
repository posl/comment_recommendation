def main():
    S = input()
    N = len(S)
    result = [0] * N
    i = 0
    while i < N:
        if S[i] == 'R':
            j = i
            while j < N and S[j] == 'R':
                j += 1
            result[j-1] += (j - i) // 2 + (i - j + 1) // 2
            result[j] += (j - i + 1) // 2 + (i - j) // 2
            i = j
        else:
            j = i
            while j < N and S[j] == 'L':
                j += 1
            result[j-1] += (j - i) // 2 + (i - j + 1) // 2
            result[j] += (j - i + 1) // 2 + (i - j) // 2
            i = j
    print(' '.join(map(str, result)))
