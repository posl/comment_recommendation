def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    scores = [k-q for _ in range(n)]
    for i in range(q):
        scores[a[i]-1] += 1
    for i in range(n):
        if scores[i] > 0:
            print("Yes")
        else:
            print("No")
