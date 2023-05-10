def main():
    x,y = [int(i) for i in input().strip().split(" ")]
    if x>=y:
        print(0)
    else:
        print(int(y-x))

if __name__ == '__main__':
    main()