def count_bottoms(s):
    #print(s)
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    return count

if __name__ == '__main__':
    count_bottoms()