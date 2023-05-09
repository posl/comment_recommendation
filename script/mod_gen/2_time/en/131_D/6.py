def main():
    N = int(input())
    job = []
    for i in range(N):
        a, b = map(int, input().split())
        job.append([a, b])
    job.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += job[i][0]
        if time > job[i][1]:
            print('No')
            return
    print('Yes')
main()

if __name__ == '__main__':
    main()