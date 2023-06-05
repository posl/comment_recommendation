def main():
    print("hello world!")
    k = int(input())
    #print(k)
    if k == 2:
        print(2)
    else:
        n = k
        while n%2 == 0:
            n = n/2
        if n == 1:
            print(k)
        else:
            print(int(n)+1)
