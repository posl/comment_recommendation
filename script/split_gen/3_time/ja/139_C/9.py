def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            continue
        if H[i] <= H[i-1]:
            count += 1
    print(count)
