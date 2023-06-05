def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    for i in range(k):
        a = [a[i-1] for i in a]
    print(a[0])
