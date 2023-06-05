def main():
    num = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = []
    for i in range(q):
        bc.append(list(map(int, input().split())))
    sum = 0
    for i in range(num):
        sum += a[i]
    for i in range(q):
        sum = sum + bc[i][1] * a.count(bc[i][0]) - bc[i][0] * a.count(bc[i][0])
        print(sum)
