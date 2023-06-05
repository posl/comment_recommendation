def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    town = 1
    for i in range(K):
        town = A[town - 1]
    print(town)
