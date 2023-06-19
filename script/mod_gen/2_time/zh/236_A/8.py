def problem236_a():
    S = input()
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))

if __name__ == '__main__':
    problem236_a()