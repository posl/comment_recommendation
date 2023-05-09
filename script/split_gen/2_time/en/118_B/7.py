def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(sum(all(i in A[j] for j in range(N)) for i in range(1, M+1)))
