def main():
    n = int(input())
    tasks = []
    for i in range(n):
        a, b = map(int, input().split())
        tasks.append((a, b))
    tasks.sort(key=lambda x: x[1])
    time = 0
    for task in tasks:
        time += task[0]
        if time > task[1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()