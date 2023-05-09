def main():
    s = input()
    s_set = set(s)
    if len(s_set) == len(s) and s.islower() == False and s.isupper() == False:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()