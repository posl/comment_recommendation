def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a = [max(a[j], a[j+1]) for j in range(0, len(a), 2)]
    print(a.index(min(a)) + 1)
