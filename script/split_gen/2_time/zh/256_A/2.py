def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        sum = 0
        for j in range(n):
            if a[j] > x[i]:
                sum += a[j] - x[i]
            else:
                sum += x[i] - a[j]
        print(sum)
