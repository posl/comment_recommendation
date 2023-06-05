def main():
    N = int(input())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    work.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print("No")
            return
    print("Yes")
