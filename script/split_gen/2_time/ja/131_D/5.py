def main():
    n = int(input())
    job = []
    for i in range(n):
        a, b = map(int, input().split())
        job.append([b, a])
    job.sort()
    time = 0
    for i in range(n):
        time += job[i][1]
        if time > job[i][0]:
            print("No")
            return
    print("Yes")
    return
