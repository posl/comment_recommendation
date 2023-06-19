def lunlun(n):
    queue = [1,2,3,4,5,6,7,8,9]
    for i in range(n):
        ret = queue.pop(0)
        if ret%10 != 0:
            queue.append(ret*10 + ret%10 - 1)
        queue.append(ret*10 + ret%10)
        if ret%10 != 9:
            queue.append(ret*10 + ret%10 + 1)
    return ret
n = int(input())
print(lunlun(n))
