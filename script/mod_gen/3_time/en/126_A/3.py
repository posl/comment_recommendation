def problem126_a():
    N, K = map(int, input().split())
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])
problem126_a()

if __name__ == '__main__':
    problem126_a()