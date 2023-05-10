def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    time = 0
    for i in range(N):
        if time <= T:
            ans += 1
            time += A[i]
        else:
            break
    print(ans, time - A[ans - 1])

if __name__ == '__main__':
    main()