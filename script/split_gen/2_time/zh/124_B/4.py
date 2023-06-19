def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        for j in range(i):
            if H[j] > H[i]:
                break
        else:
            count += 1
    print(count)
