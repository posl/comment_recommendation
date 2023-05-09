def main():
    n,m = map(int, input().split())
    an = list(map(int, input().split()))
    cm = list(map(int, input().split()))
    bn = [0] * (m+1)
    for i in range(m+1):
        bn[i] = cm[i] - sum([bn[j] * an[i-j] for j in range(i)])
    print(*bn)

if __name__ == '__main__':
    main()