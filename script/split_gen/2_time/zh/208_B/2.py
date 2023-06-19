def main():
    p = int(input())
    count = 0
    for i in range(10, 0, -1):
        count += p // factorial(i)
        p = p % factorial(i)
    print(count)
