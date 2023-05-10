def lunlun_number():
    K = int(input())
    q = []
    for i in range(1,10):
        q.append(i)
    for i in range(K):
        x = q.pop(0)
        if x % 10 != 0:
            q.append(10*x + x%10 - 1)
        q.append(10*x + x%10)
        if x % 10 != 9:
            q.append(10*x + x%10 + 1)
    print(x)

if __name__ == '__main__':
    lunlun_number()