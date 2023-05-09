def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = N
    count = 0
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)
