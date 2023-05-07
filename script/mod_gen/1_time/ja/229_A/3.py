def main():
    S1 = input()
    S2 = input()
    if S1[0] == "#" and S1[1] == "#":
        print("Yes")
    elif S2[0] == "#" and S2[1] == "#":
        print("Yes")
    elif S1[0] == "#" and S2[1] == "#":
        print("Yes")
    elif S1[1] == "#" and S2[0] == "#":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()