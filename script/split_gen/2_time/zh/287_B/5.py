def main():
    n = int(input())
    flag = 0
    for i in range(n):
        s = input()
        if s == "For":
            flag += 1
        else:
            flag -= 1
    if flag > 0:
        print("Yes")
    else:
        print("No")
