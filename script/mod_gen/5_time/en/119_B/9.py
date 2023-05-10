def get_input():
    n = int(input())
    x = []
    u = []
    for i in range(n):
        a,b = input().split()
        x.append(float(a))
        u.append(b)
    return n,x,u

if __name__ == '__main__':
    get_input()