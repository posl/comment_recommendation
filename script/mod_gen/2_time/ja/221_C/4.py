def main():
    N = input()
    max = 0
    for i in range(1,len(N)):
        A = N[:i]
        B = N[i:]
        if int(A)*int(B) > max:
            max = int(A)*int(B)
    print(max)

if __name__ == '__main__':
    main()