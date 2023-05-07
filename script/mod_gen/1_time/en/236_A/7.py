def swap(a,b,word):
    a = a - 1
    b = b - 1
    word[a], word[b] = word[b], word[a]
    return word

if __name__ == '__main__':
    swap()