def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(n)
    #print(len(a))
    #print(len(b))
    a_b = []
    for i in range(n):
        a_b.append([a[i], b[i]])
    #print(a_b)
    #print(a_b[0][0])
    #print(a_b[0][1])
    #print(a_b[1][0])
    #print(a_b[1][1])
    #print(a_b[2][0])
    #print(a_b[2][1])
    a_b.sort()
    #print(a_b)
    #print(a_b[0][0])
    #print(a_b[0][1])
    #print(a_b[1][0])
    #print(a_b[1][1])
    #print(a_b[2][0])
    #print(a_b[2][1])
    d = [0] * n
    #print(d)
    for i in range(n):
        d[i] = [0, 0]
    #print(d)
    #print(d[0][0])
    #print(d[0][1])
    #print(d[1][0])
    #print(d[1][1])
    #print(d[2][0])
    #print(d[2][1])
    for i in range(n):
        d[i][0] = a_b[i][0]
        d[i][1] = a_b[i][0] + a_b[i][1] - 1
    #print(d)
    #print(d[0][0])
    #print(d[0][1])
    #print(d[1][0])
    #print(d[1][1])
    #print(d[2][0])
    #print(d[2][1])
    #print(d[0][0])
    #print(d[0][1])
    #print(d[1][0])
    #print(d[1][1])
    #print(d[2][0])
    #print(d[2][1])
    #print(d[0][0])
    #print(d[0][

if __name__ == '__main__':
    main()