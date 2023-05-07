def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(2**n - a.index(min(a)) - 1)
