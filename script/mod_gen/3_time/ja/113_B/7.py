def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    T = T - A
    ans = 0
    for i in range(N):
        if T - H[i]*0.006 > 0:
            if T - H[i]*0.006 < T - H[ans]*0.006:
                ans = i
        else:
            if T - H[i]*0.006 > T - H[ans]*0.006:
                ans = i
    print(ans+1)

if __name__ == '__main__':
    main()