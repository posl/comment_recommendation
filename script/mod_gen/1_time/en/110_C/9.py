def main():
    S = input()
    T = input()
    # 1. Check if |S| = |T|
    if len(S) != len(T):
        print("No")
        return
    # 2. Check if |S| = |T| = 26
    if len(S) == 26:
        print("Yes")
        return
    # 3. Check if S and T have the same set of characters
    if set(S) == set(T):
        print("Yes")
        return
    # 4. Check if S and T have the same number of distinct characters
    if len(set(S)) == len(set(T)):
        print("Yes")
        return
    print("No")
    return
main()

if __name__ == '__main__':
    main()