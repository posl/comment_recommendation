def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = 1000000
    for i in range(N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)
