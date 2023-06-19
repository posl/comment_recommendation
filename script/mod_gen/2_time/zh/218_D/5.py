def find(a,b):
    count = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] == a[j] and b[i] == b[j]:
                count += 1
    return count

if __name__ == '__main__':
    find()