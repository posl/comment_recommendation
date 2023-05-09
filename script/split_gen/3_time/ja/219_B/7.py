def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    result = ""
    for i in T:
        if i == "1":
            result += S1
        elif i == "2":
            result += S2
        else:
            result += S3
    print(result)
main()
