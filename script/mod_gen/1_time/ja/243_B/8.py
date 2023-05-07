def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = {a: i for i, a in enumerate(A)}
    b = {b: i for i, b in enumerate(B)}
    c = {a: b for a, b in a.items() if a in b}
    print(len(c))
    print(sum([1 for a, b in a.items() if a in b and a[b] != b[a]]))

if __name__ == '__main__':
    main()