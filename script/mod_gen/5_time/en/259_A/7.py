def find_height(n,m,x,t,d):
    height = t
    for i in range(1,x):
        height += d
    for i in range(x,n):
        height += d
    return height

if __name__ == '__main__':
    find_height()