def main():
    N = int(input())
    A = list(map(int, input().split()))
    min_score = min(A)
    A.remove(min_score)
    print(A.index(min(A)) + 2)

if __name__ == '__main__':
    main()