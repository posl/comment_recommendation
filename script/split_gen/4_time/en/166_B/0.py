def main():
    n, k = map(int, input().split())
    a = [0] * n
    for i in range(k):
        d = int(input())
        for j in map(int, input().split()):
            a[j - 1] += 1
    print(a.count(0))
