def shiritori(N):
    words = []
    for i in range(N):
        word = input()
        if word in words:
            return False
        if i > 0 and words[-1][-1] != word[0]:
            return False
        words.append(word)
    return True
