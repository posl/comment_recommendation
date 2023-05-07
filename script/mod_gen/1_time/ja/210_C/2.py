def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    color = []
    for i in range(N-K+1):
        color.append(len(set(c[i:i+K])))
    print(max(color))

if __name__ == '__main__':
    main()