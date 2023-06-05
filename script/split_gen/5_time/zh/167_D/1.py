def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    i = 0
    count = 0
    while True:
        count += 1
        i = A[i] - 1
        if count == K:
            print(i + 1)
            break
