def main():
    a,b,c,d,e = map(int,input().split())
    print(max((a+9)//10*10,(b+9)//10*10,(c+9)//10*10,(d+9)//10*10,(e+9)//10*10)+e)

if __name__ == '__main__':
    main()