def main():
    N = int(input())
    res = 0
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            for k in range(j, N+1, j):
                if k % j == 0:
                    res += 1
    print(res)
