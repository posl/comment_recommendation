def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(N):
        for y in range(x+1, N):
            for z in range(y+1, N):
                for w in range(z+1, N):
                    if A[x] + A[y] + A[z] + A[w] == P + Q + R:
                        ans = 1
    if ans == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()