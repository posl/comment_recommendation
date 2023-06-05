def main():
    #n,s,d = map(int, input().split())
    #x = []
    #y = []
    #for i in range(n):
    #    x_i, y_i = map(int, input().split())
    #    x.append(x_i)
    #    y.append(y_i)
    n, s, d = 7, 100, 100
    x = [10, 12, 192, 154, 142, 20, 17]
    y = [11, 67, 79, 197, 158, 25, 108]
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')
