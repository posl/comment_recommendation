def main():
    n = int(input())
    j = [list(map(int, input().split())) for i in range(n)]
    j = sorted(j, key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += j[i][0]
        if t > j[i][1]:
            print("No")
            return
    print("Yes")
