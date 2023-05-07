def main():
    N, W = map(int, input().split())
    time = [0] * 200001
    for _ in range(N):
        S, T, P = map(int, input().split())
        time[S] += P
        time[T] -= P
    for i in range(200000):
        time[i + 1] += time[i]
        if time[i] > W:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()