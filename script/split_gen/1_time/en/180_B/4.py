def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(abs(x) for x in a))
    print((sum(x*x for x in a))**0.5)
    print(max(abs(x) for x in a))
