def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-2):
        if d[i][0] == d[i][1] == d[i+1][0] == d[i+1][1] == d[i+2][0] == d[i+2][1]:
            print("Yes")
            return
    print("No")
