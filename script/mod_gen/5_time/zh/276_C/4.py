def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    a[i:] = a[len(a)-1:i-1:-1]
    return True
n = int(input())
p = list(map(int, input().split()))
a = list(range(1, n+1))
i = 1
while True:
    if p == a:
        print(*a)
        break
    next_permutation(a)
    i += 1

if __name__ == '__main__':
    next_permutation()