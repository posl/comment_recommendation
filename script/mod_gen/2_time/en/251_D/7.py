def main():
    W = int(input())
    N = 0
    A = []
    while W > 0:
        if W % 2 == 0:
            N += 1
            A.append(2)
            W -= 2
        else:
            N += 2
            A.append(3)
            A.append(3)
            W -= 6
    print(N)
    print(*A)

if __name__ == '__main__':
    main()