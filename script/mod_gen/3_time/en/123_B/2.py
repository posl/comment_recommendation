def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(min((A+9)//10*10, (B+9)//10*10, (C+9)//10*10, (D+9)//10*10, (E+9)//10*10) + max(A, B, C, D, E))

if __name__ == '__main__':
    main()