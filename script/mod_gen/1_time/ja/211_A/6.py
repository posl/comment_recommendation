def main():
    # A B
    A, B = map(int, input().split())
    C = ((A-B)/(3)) +B
    print(C)
    return

if __name__ == '__main__':
    main()