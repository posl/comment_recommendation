def main():
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())
    s.sort()
    max=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            max+=1
        else:
            max=1
        if max>1:
            print(s[i])

if __name__ == '__main__':
    main()