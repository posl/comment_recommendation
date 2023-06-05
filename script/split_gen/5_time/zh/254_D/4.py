def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            if isSquareNum(i*j):
                if i == j:
                    count += 1
                else:
                    count += 2
    print(count)
