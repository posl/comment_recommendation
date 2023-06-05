def problems229_b():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if a+b >= 10**18:
        print('Hard')
    else:
        print('Easy')

if __name__ == '__main__':
    problems229_b()