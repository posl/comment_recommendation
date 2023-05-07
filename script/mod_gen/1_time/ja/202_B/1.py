def main():
    s = input()
    ans = ""
    for i in s:
        if i == "6":
            ans = "9" + ans
        elif i == "9":
            ans = "6" + ans
        else:
            ans = i + ans
    print(ans)

if __name__ == '__main__':
    main()