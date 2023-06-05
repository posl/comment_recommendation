def main():
    n=int(input())
    count=0
    for i in range(1,n+1,2):
        if divisors(i)==8:
            count+=1
    print(count)

if __name__ == '__main__':
    main()