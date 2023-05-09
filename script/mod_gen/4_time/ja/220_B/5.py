def n_to_10(n, k):
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (k ** (len(n)-1-i))
    return ans
k = int(input())
a, b = input().split()
a = n_to_10(a, k)
b = n_to_10(b, k)
print(a*b)

if __name__ == '__main__':
    n_to_10()