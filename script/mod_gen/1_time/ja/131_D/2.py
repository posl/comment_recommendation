def main():
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    work.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()