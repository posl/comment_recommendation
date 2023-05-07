def main():
    a,b=map(int,input().split())
    print(b-a-(b-a+1)*(b-a)//2)
main()

if __name__ == '__main__':
    main()