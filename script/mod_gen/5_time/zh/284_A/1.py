def problems284_a():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-i-1])

if __name__ == '__main__':
    problems284_a()