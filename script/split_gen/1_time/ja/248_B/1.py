def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while A < B:
        A *= K
        cnt += 1
    print(cnt)
