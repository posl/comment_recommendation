def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        d = int(input())
        a.extend(map(int, input().split()))
    a = set(a)
    print(n - len(a))
