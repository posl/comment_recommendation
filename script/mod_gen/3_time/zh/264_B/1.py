def problems264_b():
    r,c=input().split()
    r=int(r)
    c=int(c)
    if r%2==0:
        if c%2==0:
            print('黑色')
        else:
            print('白色')
    else:
        if c%2==0:
            print('白色')
        else:
            print('黑色')

if __name__ == '__main__':
    problems264_b()