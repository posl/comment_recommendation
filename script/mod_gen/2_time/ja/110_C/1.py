def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    if count <= 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()