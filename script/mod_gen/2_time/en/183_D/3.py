def main():
    N, W = map(int, input().split())
    usage = [0] * 200001
    for i in range(N):
        S, T, P = map(int, input().split())
        usage[S] += P
        usage[T] -= P
    for i in range(1, 200001):
        usage[i] += usage[i - 1]
        if usage[i] > W:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()