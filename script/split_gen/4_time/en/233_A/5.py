def main():
    X,Y = map(int, input().split())
    ans = (Y - X) % 10
    if ans == 0:
        ans = 0
    elif ans == 1:
        ans = 1
    elif ans == 2:
        ans = 2
    elif ans == 3:
        ans = 3
    elif ans == 4:
        ans = 4
    elif ans == 5:
        ans = 5
    elif ans == 6:
        ans = 6
    elif ans == 7:
        ans = 7
    elif ans == 8:
        ans = 8
    elif ans == 9:
        ans = 9
    print(ans)
