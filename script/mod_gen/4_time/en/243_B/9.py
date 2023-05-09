def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(len(set(A) & set(B)))
    print(len(set(A) & set(B, i != j)))

if __name__ == '__main__':
    main()