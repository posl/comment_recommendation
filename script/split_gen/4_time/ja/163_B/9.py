def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(n-sum(a),-1))
