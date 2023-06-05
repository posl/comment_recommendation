def check_shiritori(words):
    if len(words) == len(set(words)):
        for i in range(0, len(words)-1):
            if words[i][-1] != words[i+1][0]:
                return False
        return True
    else:
        return False
n = int(input())
words = []
for i in range(n):
    words.append(input())
