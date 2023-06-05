def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        j = 0
        while j < n:
            if x[i] <= a[j]:
                print(n-j)
                break
            j += 1
