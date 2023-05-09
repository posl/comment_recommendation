def main():
    S = input()
    a, b = map(int, input().split())
    a = a - 1
    b = b - 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))
