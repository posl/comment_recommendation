def main():
    s = input().split()
    t = input().split()
    if len(set(s)) == 3 and len(set(t)) == 3:
        print("Yes")
    elif len(set(s)) == 2 and len(set(t)) == 2:
        print("Yes")
    elif len(set(s)) == 1 and len(set(t)) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()