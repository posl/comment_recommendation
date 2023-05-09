def num_of_arithmetic_progressions(n):
    result = 0
    for i in range(1, n+1):
        if (n-i) % i == 0:
            result += 1
    return result
n = int(input())
print(num_of_arithmetic_progressions(n))

if __name__ == '__main__':
    num_of_arithmetic_progressions()