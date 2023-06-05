def main():
    a,b,x=map(int,input().split())
    if x<=a*a*b/2:
        ans=90-2*x/(a**3)*180
    else:
        ans=2*(a**2*b-x)/(a**2)*180
    print(ans)

if __name__ == '__main__':
    main()