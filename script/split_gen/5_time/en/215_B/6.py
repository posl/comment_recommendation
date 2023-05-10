def main():
    n = int(input())
    for i in range(60):
        if 2**i > n:
            print(i-1)
            break
