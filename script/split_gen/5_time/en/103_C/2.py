def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max([sum([x % i for x in a]) for i in range(1, 1001)]))
