def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    scores = [k - q for _ in range(n)]
    for i in a:
        scores[i - 1] += 1
    for i in scores:
        if i > 0:
            print("Yes")
        else:
            print("No")
