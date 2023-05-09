def main():
    N = int(input())
    work = []
    for i in range(N):
        a,b = map(int, input().split())
        work.append((b,a))
    work.sort()
    time = 0
    for i in range(N):
        time += work[i][1]
        if time > work[i][0]:
            print("No")
            return
    print("Yes")
