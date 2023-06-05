def get_divisor(n):
    """求一个数的约数"""
    if n == 1:
        return [1]
    else:
        i = 1
        divisor = []
        while i*i <= n:
            if n % i == 0:
                divisor.append(i)
                if i*i != n:
                    divisor.append(n//i)
            i += 1
        divisor.sort()
        return divisor
n = int(input())
divisor = get_divisor(n)
for i in divisor:
    print(i)

if __name__ == '__main__':
    get_divisor()