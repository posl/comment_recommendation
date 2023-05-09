def main():
    N = int(input())
    for i in range(0, 60):
        if (2**i) > N:
            print(i-1)
            break
