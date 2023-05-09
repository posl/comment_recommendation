def main():
    x = input()
    if x[2] in ['0','1','2']:
        print(int(x[0])-1)
    elif x[2] in ['3','4','5','6']:
        print(int(x[0]))
    else:
        print(int(x[0])+1)

if __name__ == '__main__':
    main()