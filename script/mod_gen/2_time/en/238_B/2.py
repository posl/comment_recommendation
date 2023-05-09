def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [360 - a for a in A]
    A = [a if a <= 180 else 360 - a for a in A]
    print(min(A))

if __name__ == '__main__':
    main()