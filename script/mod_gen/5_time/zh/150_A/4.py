def problems150_a():
    k, x = map(int, input().split())
    if k*500 >= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    problems150_a()