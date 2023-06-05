def main():
    n = int(input())
    flag = False
    for i in range(0, n // 4 + 1):
        for j in range(0, n // 7 + 1):
            if 4 * i + 7 * j == n:
                flag = True
                break
    if flag:
        print("Yes")
    else:
        print("No")
