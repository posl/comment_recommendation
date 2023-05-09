def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count
n = int(input())
count = 0
for i in range(1, n+1):
    if count_divisors(i) == 75:
        count += 1
print(count)
Python3で出力するとTime Limit Exceededになってしまう。Python2で出力したらACになった。

if __name__ == '__main__':
    count_divisors()