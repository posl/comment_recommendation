def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    answer = ""
    for i in range(len(t)):
        if t[i] == "1":
            answer += s1
        elif t[i] == "2":
            answer += s2
        elif t[i] == "3":
            answer += s3
    print(answer)

if __name__ == '__main__':
    main()