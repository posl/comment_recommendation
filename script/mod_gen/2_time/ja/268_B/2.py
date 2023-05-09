def main():
    s = input()
    t = input()
    if t[:len(s)] == s:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()