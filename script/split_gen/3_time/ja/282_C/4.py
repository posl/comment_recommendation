def main():
    N = int(input())
    S = input()
    i = 0
    while i < N:
        if S[i] == '"':
            j = i + 1
            while j < N:
                if S[j] == '"':
                    break
                j += 1
            k = j + 1
            while k < N:
                if S[k] != ',':
                    break
                k += 1
            for l in range(i, j + 1):
                if l % 2 == 1:
                    S = S[:l] + '.' + S[l + 1:]
            i = k - 1
        i += 1
    print(S)
