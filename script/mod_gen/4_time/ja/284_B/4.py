def count_odd(n, a):
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    return count
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_odd(n, a))

if __name__ == '__main__':
    count_odd()