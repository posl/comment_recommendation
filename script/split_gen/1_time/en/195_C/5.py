def main():
    N = input()
    N = N[::-1]
    print(sum([i for i in range(len(N)) if i % 3 == 2]))
