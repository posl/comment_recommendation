def main():
    a,b,c=map(int,input().split())
    result=-1
    for i in range(a,b+1):
        if i%c==0:
            result=i
            break
    print(result)

if __name__ == '__main__':
    main()