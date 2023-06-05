def main():
    H,A=map(int,input().split())
    ans=H//A
    if H%A!=0:
        ans+=1
    print(ans)

if __name__ == '__main__':
    main()