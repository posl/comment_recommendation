def shiritori(words):
    if len(words) != len(set(words)):
        return "No"
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1]:
            return "No"
    return "Yes"
n = int(input())
words = [input() for i in range(n)]
print(shiritori(words))
