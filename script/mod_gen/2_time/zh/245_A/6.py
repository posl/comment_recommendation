def main():
    A,B,C,D = map(int,input().split())
    if A*60+B < C*60+D:
        print("高桥")
    else:
        print("青木")

if __name__ == '__main__':
    main()