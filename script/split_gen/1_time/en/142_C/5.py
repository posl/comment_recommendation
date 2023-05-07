def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    index = [i for i in range(N+1)]
    index = [0] + index
    for i in range(1, N+1):
        index[A[i]] = i
    for i in range(1, N+1):
        print(index[i])
