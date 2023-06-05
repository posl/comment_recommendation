def main():
    s = input()
    s = s.replace("()", "")
    while True:
        if s.find("()") == -1:
            break
        s = s.replace("()", "")
    if len(s) == 0:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()