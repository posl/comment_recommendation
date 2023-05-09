def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()