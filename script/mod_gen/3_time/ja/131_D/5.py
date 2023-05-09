def main():
    n = int(input())
    job_list = []
    for i in range(n):
        a, b = map(int, input().split())
        job_list.append([a, b])
    job_list.sort(key=lambda x: x[1])
    time = 0
    for a, b in job_list:
        time += a
        if time > b:
            print("No")
            break
    else:
        print("Yes")

if __name__ == '__main__':
    main()