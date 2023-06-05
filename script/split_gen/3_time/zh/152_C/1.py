def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = 10**9+1
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)
