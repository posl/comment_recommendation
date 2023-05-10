def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    min = N
    count = 0
    for i in range(N):
        if min > P[i]:
            min = P[i]
            count += 1
    print(count)
