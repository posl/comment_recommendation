def main():
    A,B,C,X = map(int,input().split())
    count=0
    if A<=X:
        count+=1
    if A+1<=X and X<=B:
        count+=C
    print(count/(B-A))

if __name__ == '__main__':
    main()