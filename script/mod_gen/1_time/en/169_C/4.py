def main():
    A, B = map(str, input().split())
    A = int(A)
    B = int(float(B) * 100)
    print((A * B) // 100)

if __name__ == '__main__':
    main()