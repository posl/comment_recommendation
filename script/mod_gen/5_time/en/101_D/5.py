def S(n):
    return sum([int(i) for i in str(n)])
K = int(input())
n = 1
while K > 0:
    if n/S(n) <= (n+1)/S(n+1):
        print(n)
        K -= 1
    n += 1

if __name__ == '__main__':
    S()