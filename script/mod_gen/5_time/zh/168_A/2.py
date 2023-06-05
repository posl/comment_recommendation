def main():
    num = int(input())
    num = num % 10
    if num in [2,4,5,7,9]:
        print("hon")
    elif num in [0,1,6,8]:
        print("pon")
    else:
        print("bon")

if __name__ == '__main__':
    main()