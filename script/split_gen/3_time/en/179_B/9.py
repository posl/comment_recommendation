def main():
    #入力
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    #処理
    count = 0
    for i in range(n):
        if d[i][0] == d[i][1]:
            count += 1
            if count == 3:
                print("Yes")
                return
        else:
            count = 0
    print("No")
    return
