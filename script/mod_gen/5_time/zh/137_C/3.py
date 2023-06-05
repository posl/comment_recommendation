def get_word_dict(word):
    word_dict = {}
    for i in range(len(word)):
        if word[i] in word_dict:
            word_dict[word[i]] += 1
        else:
            word_dict[word[i]] = 1
    return word_dict

if __name__ == '__main__':
    get_word_dict()