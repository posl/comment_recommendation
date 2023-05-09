def main():
    N = int(input())
    print(N - sum([N // 10**d * 2 - (N // 10**(d+1) * 2) for d in range(6)]) - sum([N // 8**d * 2 - (N // 8**(d+1) * 2) for d in range(6)]) + sum([N // (8**d * 10**d) * 2 - (N // (8**(d+1) * 10**(d+1)) * 2) for d in range(6)]))
