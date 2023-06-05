def main():
    N = int(input())
    S = input()
    flag = False
    for i in range(1, N):
        if S[:i] == S[i:]:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()