def main():
    T=int(input())
    for _ in range(T):
        a,s=map(int,input().split())
        if a>s:
            print("No")
            continue
        if a==s:
            print("Yes")
            continue
        if s%2==0 and a%2==0:
            print("Yes")
            continue
        if s%2==1 and a%2==1:
            print("Yes")
            continue
        print("No")

if __name__ == '__main__':
    main()