def count(n):
    ans = 0
    for i in range(1, n):
        ans += (n-1)//i
    return ans
n = int(input())
print(count(n))

if __name__ == '__main__':
    count()