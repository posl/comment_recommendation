def main():
    n, m = map(int, input().split())
    p_s = [input().split() for _ in range(m)]
    p_s = [[int(p), s] for p, s in p_s]
    p_s.sort(key=lambda x: x[0])
    p_s = [[p, s] for p, s in p_s if s == 'AC']
    p_s = [p for p, s in p_s]
    p_s = set(p_s)
    print(len(p_s), m - len(p_s))

if __name__ == '__main__':
    main()