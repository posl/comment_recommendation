def main():
    S = input()
    Q = int(input())
    reverse = False
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            reverse = not reverse
        elif query[1] == "1":
            if reverse:
                S += query[2]
            else:
                S = query[2] + S
        else:
            if reverse:
                S = query[2] + S
            else:
                S += query[2]
    print(S[::-1] if reverse else S)

if __name__ == '__main__':
    main()