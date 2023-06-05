def exchange(x):
    result = 0
    result += (x // 500) * 1000
    result += ((x % 500) // 5) * 5
    return result

if __name__ == '__main__':
    exchange()