def main():
    s = input().rstrip()
    t = "o" + s + "o"
    if t.find("oo") == -1:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()