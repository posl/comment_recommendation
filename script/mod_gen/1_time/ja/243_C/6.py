def main():
    N = int(input())
    Point = []
    for i in range(N):
        x, y = map(int, input().split())
        Point.append((x, y))
    S = input()
    for i in range(N):
        if S[i] == 'R':
            for j in range(i+1, N):
                if S[j] == 'L':
                    if Point[i][0] < Point[j][0]:
                        if Point[i][1] == Point[j][1]:
                            print("Yes")
                            return
    print("No")

if __name__ == '__main__':
    main()