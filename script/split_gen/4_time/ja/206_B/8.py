def main():
    N = int(input())
    i = 1
    while True:
        if N <= i*(i+1)/2:
            print(i)
            break
        i += 1
