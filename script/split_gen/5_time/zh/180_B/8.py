def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(n)]))
    print(sum([x[i] ** 2 for i in range(n)]) ** 0.5)
    print(max([abs(x[i]) for i in range(n)]))
