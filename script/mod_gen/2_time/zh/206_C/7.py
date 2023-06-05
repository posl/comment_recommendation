def sum(n):
    return int(n*(n+1)/2)
N = int(input())
x = 0
while sum(x) < N:
    x += 1
print(x)

if __name__ == '__main__':
    sum()