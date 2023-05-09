def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for a in A:
        if a < P:
            cnt += 1
    print(cnt)
