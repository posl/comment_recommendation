def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    v.sort()
    for i in range(n-1):
        v[i+1] = (v[i] + v[i+1])/2
    print(v[-1])

if __name__ == '__main__':
    main()