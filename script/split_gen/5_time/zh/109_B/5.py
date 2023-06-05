def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        word = input()
        if word in words:
            return 'No'
        if i > 0 and words[i-1][-1] != word[0]:
            return 'No'
        words.append(word)
    return 'Yes'
