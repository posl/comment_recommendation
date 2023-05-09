def exchange(x):
    return x // 500 * 1000 + (x % 500) // 5 * 5
x = int(input())
print(exchange(x))

if __name__ == '__main__':
    exchange()