def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    print(min(max(a_i, b_j) for a_i, b_j in zip(a, b)))

if __name__ == '__main__':
    main()