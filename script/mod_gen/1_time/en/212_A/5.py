def main():
    A, B = input().split()
    if int(A) > 0 and int(B) == 0:
        print("Gold")
    elif int(A) == 0 and int(B) > 0:
        print("Silver")
    elif int(A) > 0 and int(B) > 0:
        print("Alloy")

if __name__ == '__main__':
    main()