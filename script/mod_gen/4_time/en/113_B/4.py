def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H = [T - h * 0.006 for h in H]
    diff = [abs(A - h) for h in H]
    print(diff.index(min(diff)) + 1)

if __name__ == '__main__':
    main()