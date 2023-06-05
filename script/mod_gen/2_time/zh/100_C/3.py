def div2(num):
    count = 0
    while True:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            break
    return count
N = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(N):
    count += div2(a[i])
print(count)

if __name__ == '__main__':
    div2()