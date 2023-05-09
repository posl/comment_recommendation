def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        count = 0
        for i in range(n):
            if a[i] == x:
                count += 1
            if count == k:
                print(i+1)
                break
        else:
            print(-1)
