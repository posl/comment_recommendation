def main():
    A, B, C = map(int, input().split())
    print(A/(A+B+C)*B/(A+B+C-1)*C/(A+B+C-2) + B/(A+B+C)*A/(A+B+C-1)*C/(A+B+C-2) + C/(A+B+C)*A/(A+B+C-1)*B/(A+B+C-2) + 1)

if __name__ == '__main__':
    main()