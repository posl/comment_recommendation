def main():
    a,b = input().split()
    a = list(a)
    b = list(b)
    sumA = 0
    sumB = 0
    for i in a:
        sumA += int(i)
    for i in b:
        sumB += int(i)
    print(max(sumA,sumB))

if __name__ == '__main__':
    main()