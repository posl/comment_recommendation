def main():
    a = input("请输入A：")
    a = a.split(" ")
    p = 0
    for i in range(len(a)):
        a[i] = int(a[i])
        if a[i] == 1:
            p += 0
        elif a[i] == 2:
            p += 1
        elif a[i] == 3:
            p += 2
        elif a[i] == 4:
            p += 1
    print(p)
