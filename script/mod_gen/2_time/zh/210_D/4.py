def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    c_set = set(c[:K])
    c_max = len(c_set)
    for i in range(N-K):
        c_set.remove(c[i])
        c_set.add(c[i+K])
        if len(c_set) > c_max:
            c_max = len(c_set)
    print(c_max)

if __name__ == '__main__':
    main()