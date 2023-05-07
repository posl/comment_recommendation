def main():
    #print("Enter integers A, B, and C, separated by spaces:")
    A, B, C = map(int, input().split())
    if A**2 + B**2 < C**2:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()