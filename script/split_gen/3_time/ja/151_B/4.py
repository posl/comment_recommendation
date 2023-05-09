def main():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    score = m * n - sum(a)
    if score <= k:
        if score < 0:
            print(0)
        else:
            print(score)
    else:
        print(-1)
