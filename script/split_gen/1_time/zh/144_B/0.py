def main():
    n = int(input())
    flag = False
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                flag = True
                break
    if flag:
        print("Yes")
    else:
        print("No")
