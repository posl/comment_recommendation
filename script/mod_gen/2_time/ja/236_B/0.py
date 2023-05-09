def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    for i in range(1, N + 1):
        if cnt[i] % 2 == 1:
            print(i)
            break

if __name__ == '__main__':
    main()