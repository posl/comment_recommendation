def main():
    N = int(input())
    P = list(map(int, input().split()))
    parents = [0]*N
    for i in range(N-1):
        parents[P[i]-1] += 1
    print(max(parents)+1)
