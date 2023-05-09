def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            count += 1
    if count >= 1:
        print("Yes")
    else:
        print("No")
