def lunlun(n):
    if n == 0:
        return [0]
    else:
        result = []
        for i in lunlun(n-1):
            if i%10 != 0:
                result.append(i*10 + i%10 - 1)
            result.append(i*10 + i%10)
            if i%10 != 9:
                result.append(i*10 + i%10 + 1)
        return result
k = int(input())
print(sorted(lunlun(10))[k-1])

if __name__ == '__main__':
    lunlun()