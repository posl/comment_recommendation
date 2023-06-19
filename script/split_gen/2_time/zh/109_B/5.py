def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    # print(words)
    for i in range(n-1):
        if words[i][-1] != words[i+1][0]:
            return 'No'
    for i in range(n):
        for j in range(i+1,n):
            if words[i] == words[j]:
                return 'No'
    return 'Yes'
print(shiritori())
