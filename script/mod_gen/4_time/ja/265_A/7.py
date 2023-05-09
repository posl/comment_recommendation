def main():
    x,y,n = map(int,input().split())
    min = 1000000000
    for i in range(n+1):
        for j in range(n+1):
            if i+j == n:
                if x*i+y*j < min:
                    min = x*i+y*j
    print(min)

if __name__ == '__main__':
    main()