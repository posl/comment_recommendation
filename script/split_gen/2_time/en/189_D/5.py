def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 2**(N+1) - 2**(N-S.count("OR"))
    print(ans)
