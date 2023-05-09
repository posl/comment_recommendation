def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    for i in T:
        if i == "1":
            print(S1, end = "")
        elif i == "2":
            print(S2, end = "")
        else:
            print(S3, end = "")

if __name__ == '__main__':
    main()