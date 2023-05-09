def harvest(a):
    if a <= 10:
        return 0
    else:
        return a-10
n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += harvest(a[i])
print(sum)

if __name__ == '__main__':
    harvest()