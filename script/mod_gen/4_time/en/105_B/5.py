def main():
    n = int(input())
    for i in range((n//4)+1):
        for j in range((n//7)+1):
            if (i*4)+(j*7) == n:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()