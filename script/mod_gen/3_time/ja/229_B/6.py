def main():
    a,b=map(int,input().split())
    if a+b>999999999:
        print("Hard")
    else:
        print("Easy")

if __name__ == '__main__':
    main()