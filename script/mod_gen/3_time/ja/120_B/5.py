def get_divisor(a, b):
    divisor = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisor.append(i)
    return divisor
a, b, k = map(int, input().split())
divisor = get_divisor(a, b)
divisor.sort(reverse=True)
print(divisor[k - 1])

if __name__ == '__main__':
    get_divisor()