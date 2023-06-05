def main():
    N = int(input())
    P = list(map(int, input().split()))
    min = N
    count = 0
    for i in range(N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)
