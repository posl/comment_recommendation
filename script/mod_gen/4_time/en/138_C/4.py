def main():
    N = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[-1])

if __name__ == '__main__':
    main()