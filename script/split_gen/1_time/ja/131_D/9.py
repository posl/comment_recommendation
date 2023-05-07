def main():
    N = int(input())
    task = [list(map(int, input().split())) for _ in range(N)]
    task = sorted(task, key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += task[i][0]
        if time > task[i][1]:
            print('No')
            return
    print('Yes')
