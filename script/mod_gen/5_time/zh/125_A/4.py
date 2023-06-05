def main():
    A,B,T = map(int,input().split())
    time = T + 0.5
    num = 0
    for i in range(1,time):
        if i % A == 0:
            num += B
    print(num)

if __name__ == '__main__':
    main()