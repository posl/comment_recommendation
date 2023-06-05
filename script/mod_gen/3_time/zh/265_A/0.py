def f(x,y,n):
    min = 100000000
    for i in range(0,n+1):
        for j in range(0,n+1):
            if i*3+j*1==n:
                if min>(x*i+y*j):
                    min = x*i+y*j
    return min

if __name__ == '__main__':
    f()