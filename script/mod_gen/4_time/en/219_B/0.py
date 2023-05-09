def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    for i in t:
        if i == "1":
            result += s1
        elif i == "2":
            result += s2
        else:
            result += s3
    print(result)

if __name__ == '__main__':
    main()