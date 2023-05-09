def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    min = P[0]
    count = 1
    for i in range(1, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)
