def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()