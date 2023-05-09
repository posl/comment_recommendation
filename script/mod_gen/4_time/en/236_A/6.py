def swap():
    S = input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    S = list(S)
    S[a], S[b] = S[b], S[a]
    print(''.join(S))

if __name__ == '__main__':
    swap()