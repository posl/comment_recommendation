def main():
    # Take input Here and Call solution function
    n = int(input())
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        count += 1
    print(count + 1)
