def get_count(a):
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] < a[j]:
                count += 1
    return count

if __name__ == '__main__':
    get_count()