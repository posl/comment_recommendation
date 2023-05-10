def main():
    A, B, N = map(int, input().split())
    max = 0
    for i in range(0, N + 1):
        if (A * i // B) - A * (i // B) > max:
            max = (A * i // B) - A * (i // B)
    print(max)
main()

if __name__ == '__main__':
    main()