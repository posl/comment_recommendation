def problems250_b(n,a,b):
    s = ''
    for i in range(n):
        for j in range(a):
            if i%2==0:
                s += '.'*b
            else:
                s += '#'*b
            s += '\n'
    print(s)
problems250_b(4,3,2)
problems250_b(5,1,5)
problems250_b(4,4,1)
problems250_b(1,4,4)
