def main():
    N = int(input())
    job = [list(map(int, input().split())) for _ in range(N)]
    job.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += job[i][0]
        if time > job[i][1]:
            print("No")
            return
    print("Yes")
