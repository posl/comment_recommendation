def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    count = 0
    min = 0
    for i in range(N):
        if i == 0:
            min = P[i]
            count += 1
        elif P[i] <= min:
            min = P[i]
            count += 1
    print(count)
