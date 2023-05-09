def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [x for x in range(1, 1001)]
    count = 0
    for x in c:
        flag = True
        for i in range(n):
            if not (a[i] <= x <= b[i]):
                flag = False
                break
        if flag:
            count += 1
    print(count)
