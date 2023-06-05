def main():
    n, q = map(int, input().split())
    x = [int(input()) for _ in range(q)]
    num = [i for i in range(1, n+1)]
    for i in range(q):
        #print(num)
        #print(x[i])
        #print(num.index(x[i]))
        num[num.index(x[i])], num[num.index(x[i])+1] = num[num.index(x[i])+1], num[num.index(x[i])]
    print(*num)
