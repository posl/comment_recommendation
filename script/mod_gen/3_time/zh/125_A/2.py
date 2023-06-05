def main():
    A,B,T = map(int,input().split())
    count = 0
    for i in range(1,T+1):
        if i % A == 0:
            count = count + B
    print(count)

if __name__ == '__main__':
    main()