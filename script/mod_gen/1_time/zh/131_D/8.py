def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x:x[1])
    current_time = 0
    for a, b in jobs:
        current_time += a
        if current_time > b:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()