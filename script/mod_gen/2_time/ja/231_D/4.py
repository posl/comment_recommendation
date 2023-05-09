def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    if N == 2 and M == 0:
        print("Yes")
        return
    if N == 2 and M != 0:
        print("No")
        return
    if M == 0:
        print("Yes")
        return
    AB.sort(key=lambda x: x[0])
    # print(AB)
    for i in range(M-1):
        if AB[i][1] == AB[i+1][1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()