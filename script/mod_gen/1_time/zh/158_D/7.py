def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        query = input().split()
        if query[0] == '1':
            S = S[::-1]
        else:
            if query[1] == '1':
                S = query[2] + S
            else:
                S = S + query[2]
    print(S)

if __name__ == '__main__':
    main()