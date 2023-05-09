def main():
    N, K, A = map(int, input().split())
    ans = (A + K - 1) % N
    if ans == 0:
        ans = N
    print(ans)

if __name__ == '__main__':
    main()