def main():
    a, b, x = map(int, input().split())
    if x >= a**2*b/2:
        #print('x >= a**2*b/2')
        #print('x = ', x)
        #print('a**2*b/2 = ', a**2*b/2)
        #print('x/a**2 = ', x/a**2)
        #print('b-x/a**2 = ', b-x/a**2)
        print(90 - math.degrees(math.atan2(2*(a**2*b-x), a**3)))
    else:
        #print('x < a**2*b/2')
        #print('x = ', x)
        #print('a**2*b/2 = ', a**2*b/2)
        #print('2*x/a/b = ', 2*x/a/b)
        #print('b**2-2*x/a/b = ', b**2-2*x/a/b)
        print(math.degrees(math.atan2(b**2-2*x/a/b, 2*x/a)))

if __name__ == '__main__':
    main()