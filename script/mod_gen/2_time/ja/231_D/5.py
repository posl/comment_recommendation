def main():
    N, M = map(int, input().split())
    if M == 0:
        print("Yes")
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    last = AB[0][1]
    for i in range(1, M):
        if AB[i][0] < last:
            print("No")
            return
        last = AB[i][1]
    print("Yes")

if __name__ == '__main__':
    main()