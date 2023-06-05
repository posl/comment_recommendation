def problem120_a():
    a,b,c = map(int,input().split(' '))
    if a * c > b:
        print(b // a)
    else:
        print(c)

if __name__ == '__main__':
    problem120_a()