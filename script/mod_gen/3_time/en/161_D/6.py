def lunlun(n):
    if n < 10:
        return n
    else:
        num = str(n)
        for i in range(len(num)-1):
            if abs(int(num[i]) - int(num[i+1])) > 1:
                return 0
        return n

if __name__ == '__main__':
    lunlun()