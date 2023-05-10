def main():
    v,t,s,d = map(int, input().split())
    if d/v < t or s < d/v:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()