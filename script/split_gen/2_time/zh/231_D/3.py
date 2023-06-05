def main():
    n,q = map(int, input().split())
    A = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    for i in range(q):
        count = 0
        for j in range(n):
            if A[j] >= x[i]:
                count += 1
        print(count)
