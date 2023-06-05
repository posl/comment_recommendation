def main():
    n, k = map(int, input().split())
    total = 0
    for i in range(n):
        for j in range(1, k + 1):
            total += int(str(i + 1) + '0' + str(j))
    print(total)
