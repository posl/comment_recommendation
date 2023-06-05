def reverse_print():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

if __name__ == '__main__':
    reverse_print()