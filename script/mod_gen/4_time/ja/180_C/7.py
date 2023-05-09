def get_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisor.append(i)
            if i != n//i:
                divisor.append(n//i)
    divisor.sort()
    return divisor
n = int(input())
divisor = get_divisor(n)
for i in divisor:
    print(i)

if __name__ == '__main__':
    get_divisor()