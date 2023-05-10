def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max([sum([a % A[i] for a in A]) for i in range(N)]))
