def main():
    n, x = [int(x) for x in input().split()]
    #print(n, x)
    for i in range(1, n+1):
        if x <= i*26:
            print(chr(i*64 + x))
            return
        else:
            x -= i*26
