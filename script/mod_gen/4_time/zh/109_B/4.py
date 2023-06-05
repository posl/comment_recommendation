def check_shiritori(word_list):
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            return False
        else:
            word_dict[word] = 1
    for i in range(len(word_list)-1):
        if word_list[i][-1] != word_list[i+1][0]:
            return False
    return True

if __name__ == '__main__':
    check_shiritori()