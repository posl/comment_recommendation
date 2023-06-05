def func(n,l):
    result = 0
    for i in range(n):
        tmp = 0
        j = i
        while j != -1:
            tmp += 1
            j = l[j]
        result = max(result,tmp)
    return result

if __name__ == '__main__':
    func()