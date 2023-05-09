def lunlun(n):
    if n < 10:
        return True
    else:
        n = str(n)
        for i in range(len(n)-1):
            if abs(int(n[i])-int(n[i+1])) > 1:
                return False
        return True

if __name__ == '__main__':
    lunlun()