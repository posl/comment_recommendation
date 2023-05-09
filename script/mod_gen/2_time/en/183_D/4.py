def main():
    N, W = map(int, input().split())
    time = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        S, T, P = map(int, input().split())
        time[S] += P
        time[T] -= P
    for i in range(1, len(time)):
        time[i] += time[i - 1]
    if max(time) > W:
        print('No')
    else:
        print('Yes')
main()

if __name__ == '__main__':
    main()