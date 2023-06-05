def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    result = ""
    for i in range(len(t)):
        if t[i] == '1':
            result += s1
        elif t[i] == '2':
            result += s2
        elif t[i] == '3':
            result += s3
        else:
            print("error")
    print(result)

if __name__ == '__main__':
    main()