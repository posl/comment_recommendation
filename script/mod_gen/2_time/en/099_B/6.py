def main():
    a,b = map(int,input().split())
    print(b-a-(b-a)*(b-a+1)//2)

if __name__ == '__main__':
    main()