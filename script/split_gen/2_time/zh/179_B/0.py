def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    flag = False
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")
