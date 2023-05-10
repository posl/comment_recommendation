def main():
    n = int(input())
    job = []
    for i in range(n):
        a, b = map(int, input().split())
        job.append([a, b])
    job.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += job[i][0]
        if time > job[i][1]:
            print("No")
            exit()
    print("Yes")
