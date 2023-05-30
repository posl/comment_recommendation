def main():
    N = int(input())
    P = list(map(int, input().split()))
    #print(N)
    #print(P)
    count = 0
    min = N + 1
    for i in range(N):
        if min >= P[i]:
            min = P[i]
            count += 1
    print(count)
main()
