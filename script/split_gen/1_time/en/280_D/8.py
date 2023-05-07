def main():
    import math
    k = int(input())
    if k%2 == 0:
        print(2)
        exit()
    if k%5 == 0:
        print(5)
        exit()
    for i in range(3, math.ceil(math.sqrt(k))+1, 2):
        if k%i == 0:
            print(i)
            exit()
    print(k)
main()
