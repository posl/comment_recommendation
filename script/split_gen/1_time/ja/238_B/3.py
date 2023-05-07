def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[i] - A[i-1] for i in range(1,N)]
    B.append(360 - A[N-1] + A[0])
    print(360 - max(B))
