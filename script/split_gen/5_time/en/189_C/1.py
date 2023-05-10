def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_oranges = 0
    for l in range(N):
        for r in range(l, N):
            for x in range(1, 10000):
                oranges = 0
                for i in range(l, r+1):
                    if A[i] >= x:
                        oranges += x
                if oranges > max_oranges:
                    max_oranges = oranges
    print(max_oranges)
