def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    result = ""
    for i in range(len(T)):
        if T[i] == "1":
            result += S1
        elif T[i] == "2":
            result += S2
        else:
            result += S3
    print(result)

if __name__ == '__main__':
    main()