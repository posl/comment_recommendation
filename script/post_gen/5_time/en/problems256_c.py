Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    if (h1+h2+h3) == (w1+w2+w3):
        print("1")
    else:
        print("0")

=======
Suggestion 2

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    if (h1+h2+h3) != (w1+w2+w3):
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1*h2*h3)%(10**9+7))

=======
Suggestion 4

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    print((h1+h2+h3)*(w1+w2+w3)//(h1+h2+h3+w1+w2+w3))

=======
Suggestion 5

def main():
    h1,h2,h3,w1,w2,w3 = map(int,input().split())
    if h1+w2==h2+w1 and h2+w3==h3+w2 and h1+w3==h3+w1:
        print('1')
    else:
        print('0')

=======
Suggestion 6

def main():
    h1, h2, h3, w1, w2, w3 = map(int, input().split())
    ans = 0
    ans += (h1-1)*(w1-1)
    ans += (h1-1)*(w2-1)
    ans += (h1-1)*(w3-1)
    ans += (h2-1)*(w1-1)
    ans += (h2-1)*(w2-1)
    ans += (h2-1)*(w3-1)
    ans += (h3-1)*(w1-1)
    ans += (h3-1)*(w2-1)
    ans += (h3-1)*(w3-1)
    print(ans)

=======
Suggestion 7

def f(x):
    return 1 if x == 0 else x * f(x-1)

h1, h2, h3, w1, w2, w3 = map(int, input().split())

print(f(h1+h2+h3)//f(h1)//f(h2)//f(h3)//f(w1)//f(w2)//f(w3))

=======
Suggestion 8

def solve():
    h = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]

    def is_valid(h, w):
        if sum(h) != sum(w):
            return False
        for i in range(3):
            if h[i] + h[(i + 1) % 3] < w[i] + w[(i + 1) % 3]:
                return False
        return True

    def f(n):
        return 1 if n == 0 else n * f(n - 1)

    if is_valid(h, w):
        print(f(sum(h)) // f(h[0]) // f(h[1]) // f(h[2]))
    else:
        print(0)

solve()

=======
Suggestion 9

def solve(h1,h2,h3,w1,w2,w3):
    grid = [0]*9
    for i in range(3):
        grid[i] = h1//3
        if i < h1%3:
            grid[i] += 1
    for i in range(3):
        grid[i+3] = h2//3
        if i < h2%3:
            grid[i+3] += 1
    for i in range(3):
        grid[i+6] = h3//3
        if i < h3%3:
            grid[i+6] += 1
    for i in range(3):
        grid[i*3] -= w1//3
        if i < w1%3:
            grid[i*3] -= 1
    for i in range(3):
        grid[i*3+1] -= w2//3
        if i < w2%3:
            grid[i*3+1] -= 1
    for i in range(3):
        grid[i*3+2] -= w3//3
        if i < w3%3:
            grid[i*3+2] -= 1
    if grid[0] == grid[1] == grid[2] == grid[3] == grid[4] == grid[5] == grid[6] == grid[7] == grid[8]:
        return 1
    else:
        return 0

h1,h2,h3,w1,w2,w3 = map(int,input().split())
print(solve(h1,h2,h3,w1,w2,w3))

=======
Suggestion 10

def perm(n, r):
    if n < r:
        return 0
    else:
        return fact(n) // fact(n - r)
