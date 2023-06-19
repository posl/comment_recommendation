def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += ab[i][0]
        if t > ab[i][1]:
            print("No")
            exit()
    print("Yes")
