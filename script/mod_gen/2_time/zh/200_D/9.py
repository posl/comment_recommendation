def get_count(a):
    a.sort()
    c = [0]*200
    for i in a:
        c[i%200] += 1
    count = 0
    for i in range(200):
        if c[i] > 1:
            count += c[i]*(c[i]-1)//2
    return count

if __name__ == '__main__':
    get_count()