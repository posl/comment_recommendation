def main():
    N, C = map(int, input().split())
    abcs = []
    for _ in range(N):
        abcs.append(list(map(int, input().split())))
    abcs.sort(key=lambda x: x[0])
    days = [0] * (10**9 + 1)
    for abc in abcs:
        a, b, c = abc
        days[a] += c
        days[b + 1] -= c
    for i in range(1, len(days)):
        days[i] += days[i - 1]
    days = list(map(lambda x: min(x, C), days))
    for i in range(1, len(days)):
        days[i] += days[i - 1]
    print(days[-1])

if __name__ == '__main__':
    main()