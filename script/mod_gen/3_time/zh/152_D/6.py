def count_pair(n):
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                count += 1
    return count

if __name__ == '__main__':
    count_pair()