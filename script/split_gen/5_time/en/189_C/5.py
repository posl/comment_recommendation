def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_oranges = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(1, A[j]+1):
                oranges = 0
                for l in range(i, j+1):
                    if A[l] >= k:
                        oranges += k
                if oranges > max_oranges:
                    max_oranges = oranges
    print(max_oranges)
