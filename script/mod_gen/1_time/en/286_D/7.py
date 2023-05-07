def main():
    N, X = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0])
    total = 0
    for i in range(N):
        total += AB[i][0] * AB[i][1]
        if total > X:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()