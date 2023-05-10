def main():
    n, k = map(int, input().split())
    snuke = [0] * n
    for _ in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for i in range(d):
            snuke[a[i]-1] += 1
    print(snuke.count(0))
