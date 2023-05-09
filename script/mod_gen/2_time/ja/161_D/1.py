def main():
    k = int(input())
    q = [1,2,3,4,5,6,7,8,9]
    for i in range(k):
        x = q.pop(0)
        if x % 10 > 0:
            q.append(10*x + x%10 - 1)
        q.append(10*x + x%10)
        if x % 10 < 9:
            q.append(10*x + x%10 + 1)
    print(x)

if __name__ == '__main__':
    main()