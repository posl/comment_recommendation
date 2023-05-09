def problems203_b():
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            sum += int(str(i) + '0' + str(j))
    print(sum)

if __name__ == '__main__':
    problems203_b()