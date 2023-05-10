def count(a,b):
    n = 0
    for i in range(a,b+1):
        n += 1
    return n
a,b = map(int,input().split())
print(count(a,b))

if __name__ == '__main__':
    count()