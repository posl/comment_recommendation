def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    c_set = set()
    for i in range(N-K+1):
        c_set.add(len(set(c[i:i+K])))
    print(max(c_set))

if __name__ == '__main__':
    main()