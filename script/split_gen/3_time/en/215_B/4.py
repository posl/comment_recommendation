def main():
    N = int(input())
    for k in reversed(range(61)):
        if 2**k <= N:
            print(k)
            break
