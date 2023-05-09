def main():
    # Write code here
    v,t,s,d = map(int,input().split())
    if 1 <= v <= 1000 and 1 <= t < s <= 1000 and 1 <= d <= 1000:
        if t*v <= d <= s*v:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()