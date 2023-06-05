def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = [x[i+1] - x[i] for i in range(N)]
    import math
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    def gcd_list(numbers):
        return reduce(gcd, numbers)
    print(gcd_list(d))

if __name__ == '__main__':
    main()