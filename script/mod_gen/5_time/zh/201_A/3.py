def main():
    a1,a2,a3 = map(int,input().split())
    if a3-a2 == a2-a1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()