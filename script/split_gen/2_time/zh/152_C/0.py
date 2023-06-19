def main():
    N = int(input())
    P = input().split()
    P = [int(i) for i in P]
    count = 0
    for i in range(1, N+1):
        if P[i-1] <= i:
            count += 1
    print(count)
