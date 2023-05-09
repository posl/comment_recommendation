def main():
    a, b, k = map(int, input().split())
    #print(a, b, k)
    #print(type(a), type(b), type(k))
    #print(a, b, k)
    #print(type(a), type(b), type(k))
    i = 0
    c = 0
    while True:
        i += 1
        if a % i == 0 and b % i == 0:
            c += 1
        if c == k:
            print(i)
            break
