def main():
    N = int(input())
    i = 1
    while True:
        if (i % 2 == 0) or (i % N == 0):
            print(i)
            break
        i += 1
