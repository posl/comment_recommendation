def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()

if __name__ == '__main__':
    gcd()