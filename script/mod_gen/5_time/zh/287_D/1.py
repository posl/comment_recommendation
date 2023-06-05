def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    for i in range(len_t+1):
        if (s[:i] + t[i:]).replace("?", "a") == t:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()