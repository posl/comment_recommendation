def baseK(n, k):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, k)
        nums.append(str(r))
    return ''.join(reversed(nums))
k = int(input())
a, b = map(int, input().split())
a = baseK(a, k)
b = baseK(b, k)
print(int(a) * int(b))

if __name__ == '__main__':
    baseK()