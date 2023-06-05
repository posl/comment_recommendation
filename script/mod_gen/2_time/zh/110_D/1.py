def main():
    S = input()
    T = input()
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()