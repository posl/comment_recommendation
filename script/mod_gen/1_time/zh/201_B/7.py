def problems201_b():
    n = int(input())
    data = [input().split() for _ in range(n)]
    data = sorted(data, key=lambda x: int(x[1]), reverse=True)
    print(data[1][0])

if __name__ == '__main__':
    problems201_b()