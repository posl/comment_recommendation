def main():
    a = input()
    if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
        print('Weak')
    elif (int(a[0])+1)%10 == int(a[1]) and (int(a[1])+1)%10 == int(a[2]) and (int(a[2])+1)%10 == int(a[3]):
        print('Weak')
    else:
        print('Strong')

if __name__ == '__main__':
    main()