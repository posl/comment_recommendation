def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a = a[0:n]
    a_set = set(a)
    max_even = -1
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                max_even = max(max_even, a[i] + a[j])
    print(max_even)
