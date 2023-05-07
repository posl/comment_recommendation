def main():
    n = int(input())
    for i in range((n//7)+1):
        for j in range((n//4)+1):
            if 7*i + 4*j == n:
                print("Yes")
                return
    print("No")
main()

if __name__ == '__main__':
    main()