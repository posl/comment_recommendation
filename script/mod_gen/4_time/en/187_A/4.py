def main():
    A, B = map(int, input().split())
    print(max(sum(map(int, str(A))), sum(map(int, str(B)))))

if __name__ == '__main__':
    main()