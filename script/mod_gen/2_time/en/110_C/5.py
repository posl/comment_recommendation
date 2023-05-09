def main():
    S = input()
    T = input()
    print("Yes" if sorted(S) == sorted(T) else "No")

if __name__ == '__main__':
    main()