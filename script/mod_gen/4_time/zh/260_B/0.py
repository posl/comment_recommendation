def get_input():
    n,x,y,z = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    z = int(z)
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    return n,x,y,z,a,b

if __name__ == '__main__':
    get_input()