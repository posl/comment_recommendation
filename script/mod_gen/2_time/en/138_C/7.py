def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    v.append(0)
    for i in range(N-1):
        v.append((v[i] + v[i+1]) / 2)
    print(v[-1])

if __name__ == '__main__':
    main()