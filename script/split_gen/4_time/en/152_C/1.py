def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    minP = float('inf')
    for i in range(N):
        if P[i] <= minP:
            count += 1
            minP = P[i]
    print(count)
