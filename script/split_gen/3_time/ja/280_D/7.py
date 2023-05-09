def main():
    k = int(input())
    n = 1
    while True:
        #print(n)
        if k%n == 0:
            n += 1
        else:
            print(n)
            break
