def main():
    X = int(input())
    A = 0
    B = 0
    for i in range(1, 10**6):
        if i**5 - (i-1)**5 == X:
            A = i
            B = i-1
            break
    print(A, B)

if __name__ == '__main__':
    main()