def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p.insert(0, None)
    print(max([p.count(i) for i in range(1, n + 1)]))
