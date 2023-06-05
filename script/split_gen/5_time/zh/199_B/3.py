def main():
    num = int(input())
    a = input().split()
    b = input().split()
    count = 0
    for i in range(num):
        a[i] = int(a[i])
        b[i] = int(b[i])
    for i in range(1,1001):
        flag = True
        for j in range(num):
            if i < a[j] or i > b[j]:
                flag = False
        if flag:
            count += 1
    print(count)
