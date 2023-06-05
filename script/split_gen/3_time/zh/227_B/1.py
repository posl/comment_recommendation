def get_area(a, b):
    return 4*a*b + 3*a + 3*b
n = int(input())
s = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            count += 1
        else:
            a = (s[i] + s[j]) / 2
            b = (s[i] - s[j]) / 2
            if a > 0 and b > 0 and int(a) == a and int(b) == b:
                count += 1
print(n - count)
