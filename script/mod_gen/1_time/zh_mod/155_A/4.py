def problems155_a():
    a,b,c = input().split()
    if a==b and a!=c:
        print('Yes')
    elif a==c and a!=b:
        print('Yes')
    elif b==c and b!=a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problems155_a()