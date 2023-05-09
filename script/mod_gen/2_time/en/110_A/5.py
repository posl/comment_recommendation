def main():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)
    print(max(A+B+C, A*B*C, A+B*C, A*B+C, (A+B)*C))

if __name__ == '__main__':
    main()