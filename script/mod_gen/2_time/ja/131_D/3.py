def main():
    N = int(input())
    work = []
    for i in range(N):
        A, B = map(int, input().split())
        work.append([B, A])
    work.sort()
    time = 0
    for i in range(N):
        time += work[i][1]
        if time > work[i][0]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()