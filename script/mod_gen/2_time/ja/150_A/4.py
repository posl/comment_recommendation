def main():
    k,x = map(int,input().split())
    if x >= k*500:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()