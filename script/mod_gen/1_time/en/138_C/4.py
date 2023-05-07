def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v) > 1:
        v.append((v[0] + v[1]) / 2)
        del v[0]
        del v[0]
        v.sort()
    print(v[0])

if __name__ == '__main__':
    main()