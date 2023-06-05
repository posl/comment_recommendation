def count(N):
    count = 0
    for i in range(1, N+1):
        if i < 10:
            count += 1
        else:
            if i % 10 == int(str(i)[0]):
                count += 1
    return count

if __name__ == '__main__':
    count()