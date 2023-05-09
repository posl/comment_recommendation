def main():
    N = int(input())
    work = []
    for i in range(N):
        A, B = map(int, input().split())
        work.append([A, B])
    work = sorted(work, key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print('No')
            break
    else:
        print('Yes')
