def lunlun(K):
    if K == 1:
        return 1
    else:
        return lunlun(K-1) + 1
K = int(input())
print(lunlun(K))
In the above code, I made a recursive function to find the K-th smallest lunlun number. But it is too slow to get the answer. I will try to make it faster.

if __name__ == '__main__':
    lunlun()