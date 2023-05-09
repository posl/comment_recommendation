def main():
    N = int(input())
    H = list(map(int, input().split()))
    if N == 1:
        print(1)
    else:
        count = 0
        for i in range(N):
            if i == 0:
                if H[i] <= H[i+1]:
                    count += 1
            elif i == N-1:
                if H[i] <= H[i-1]:
                    count += 1
            else:
                if H[i] <= H[i-1] and H[i] <= H[i+1]:
                    count += 1
        print(count)
