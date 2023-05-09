def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B = map(int, input().split())
print(A * B // gcd(A, B))
Sample Input 1
2 3
Sample Output 1
6
Sample Input 2
123 456
Sample Output 2
18696
Sample Input 3
100000 99999
Sample Output 3
9999900000
