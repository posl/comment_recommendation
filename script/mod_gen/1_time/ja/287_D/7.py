def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        if S[:i].endswith(T[:i]):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()