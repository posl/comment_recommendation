def main():
    N = int(input())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    work = sorted(work, key=lambda x: x[1])
    time = 0
    for a, b in work:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")
