def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            for j in range(i):
                if H[j] > H[i]:
                    break
                if j == i-1:
                    count += 1
    print(count)
