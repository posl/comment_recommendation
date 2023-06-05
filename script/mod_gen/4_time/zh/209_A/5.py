def count_ints(a,b):
    #a,b = input().split()
    #a = int(a)
    #b = int(b)
    count = 0
    for i in range(a,b+1):
        count += 1
    return count

if __name__ == '__main__':
    count_ints()