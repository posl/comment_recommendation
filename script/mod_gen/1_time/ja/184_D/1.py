def main():
    A,B,C = map(int,input().split())
    print(100*(A/(A+B+C))+100*(B/(A+B+C))+100*(C/(A+B+C))-100)

if __name__ == '__main__':
    main()