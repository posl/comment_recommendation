def main():
    n = input()
    n = int(n)
    count = 0
    if n < 1000:
        print(0)
    else:
        for i in range(1, 16):
            if n >= 1000**i:
                count += n - (1000**i) + 1
        for i in range(2, 16):
            if n >= 1000**i:
                count -= (1000**(i-1) - 1)
        print(count)
