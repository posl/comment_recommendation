def get_num(n):
    num = 0
    for i in range(1,n+1):
        num += i
        if num == n:
            return i
        elif num > n:
            return i-1
n = int(input())
ans = 0
for i in range(1,get_num(n)+1):
    ans += (n-i) % i == 0
print(ans)

if __name__ == '__main__':
    get_num()