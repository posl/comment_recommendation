def main():
    N = int(input())
    i = 1
    while True:
        if N < 111 * i:
            print(111 * i)
            return
        i += 1
