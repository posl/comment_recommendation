def problems229_b():
    a, b = map(int, input().split())
    if a + b >= 10 ** 18:
        print('Hard')
    else:
        print('Easy')

if __name__ == '__main__':
    problems229_b()