def problems280_a():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(sum([s.count("#") for s in S]))

if __name__ == '__main__':
    problems280_a()