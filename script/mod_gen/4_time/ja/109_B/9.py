def check_shiritori(words):
    for i in range(len(words)):
        if words[i] in words[:i]:
            return "No"
        if i != 0 and words[i][0] != words[i-1][-1]:
            return "No"
    return "Yes"

if __name__ == '__main__':
    check_shiritori()