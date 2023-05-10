def get_ints(): return map(int, input().split())
n = int(input())
a = list(get_ints())
b = list(get_ints())
c = list(get_ints())
ans = 0
for i in range(n):
    ans += b[a[i]-1]
    if i < n - 1 and a[i] == a[i+1] - 1:
        ans += c[a[i]-1]
print(ans)

if __name__ == '__main__':
    get_ints()