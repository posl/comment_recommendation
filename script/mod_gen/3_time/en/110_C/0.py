def main():
    S = input()
    T = input()
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(T_set):
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()