def main():
    # Take input here
    a,b,c,d,e,f,x = map(int, input().strip().split())
    # Compute the final answer and store it in ans variable
    takahashi = (a+b)*c
    aoki = (d+e)*f
    if takahashi > aoki:
        ans = "Takahashi"
    elif aoki > takahashi:
        ans = "Aoki"
    else:
        ans = "Draw"
    print(ans)

if __name__ == '__main__':
    main()