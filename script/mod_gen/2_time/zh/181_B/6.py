def sum(n):
    return int(n*(n+1)/2)
n = int(input())
result = 0
for i in range(n):
    a,b = map(int,input().split())
    result += sum(b) - sum(a-1)
print(result)

if __name__ == '__main__':
    sum()