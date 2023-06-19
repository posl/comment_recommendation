def problems243_a():
    v,a,b,c = map(int, input().split())
    if v <= a:
        print('F')
    elif v <= a + b:
        print('M')
    else:
        print('T')

if __name__ == '__main__':
    problems243_a()