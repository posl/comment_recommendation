def main():
    a,b,k = map(int,input().split())
    if a > b:
        a,b = b,a
    count = 0
    for i in range(b,0,-1):
        if a%i == 0 and b%i == 0:
            count += 1
            if count == k:
                print(i)
                break

if __name__ == '__main__':
    main()