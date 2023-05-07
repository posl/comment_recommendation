def main():
    x = input()
    x = x.split('.')
    if int(x[1]) <= 2:
        print(x[0]+'-')
    elif int(x[1]) <= 6:
        print(x[0])
    else:
        print(x[0]+'+')
main()
