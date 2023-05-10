def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_val = 0
    for m in range(1, max(A)+1):
        val = 0
        for a in A:
            val += m % a
        if val > max_val:
            max_val = val
    print(max_val)

if __name__ == '__main__':
    main()