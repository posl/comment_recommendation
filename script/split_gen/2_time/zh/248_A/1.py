def main():
    q = int(input())
    c = [0] * q
    x = [0] * q
    for i in range(q):
        c[i], x[i] = map(int, input().split())
    # print(c)
    # print(x)
    # 計算
    sum = 0
    for i in range(q):
        if c[i] == 1:
            sum += x[i]
        elif c[i] == 2:
            print(sum)
            sum = 0
        else:
            print("error")
            return
