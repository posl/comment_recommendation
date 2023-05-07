def main():
    N, P = map(int, input().split())
    L = list(map(int, input().split()))
    count = 0
    for i in range(0, N):
        if L[i] < P:
            count += 1
    print(count)
