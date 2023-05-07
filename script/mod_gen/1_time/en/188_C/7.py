def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(i+1, a) for i,a in enumerate(A)]
    A.sort(key=lambda x: x[1])
    B = [a[0] for a in A]
    while len(B) > 2:
        B = [B[i] for i in range(len(B)) if i%2 == 1]
    print(min(B))

if __name__ == '__main__':
    main()