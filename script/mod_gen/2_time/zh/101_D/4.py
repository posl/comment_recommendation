def s(n):
    return sum(map(int, str(n)))
k = int(input())
n = 1
while k > 0:
    if s(n) * n >= n:
        print(n)
        k -= 1
    n += 1

if __name__ == '__main__':
    s()