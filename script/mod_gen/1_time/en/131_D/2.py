def main():
    N = int(input())
    jobs = []
    for i in range(N):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for a, b in jobs:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()