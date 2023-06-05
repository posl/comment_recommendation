def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += ab[i][0]
        if time > ab[i][1]:
            print("No")
            return
    print("Yes")
