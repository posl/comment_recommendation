def f(a,b):
    return (a+b)*(b-a+1)//2
n = int(input())
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    ans += f(a,b)
print(ans)

if __name__ == '__main__':
    f()