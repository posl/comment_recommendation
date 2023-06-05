def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(1, n):
        if words[i] in words[0:i]:
            return 'No'
        if words[i][0] != words[i-1][-1]:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    shiritori()