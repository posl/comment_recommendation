def main():
    A, B, C = map(int, input().split())
    print(C - (A - B) if A - B < C else 0)
main()

if __name__ == '__main__':
    main()