def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1000):
        for j in range(1000):
            if i**5 - j**5 == X:
                A = i
                B = j
    print(A, B)

if __name__ == '__main__':
    main()