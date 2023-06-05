def checkShiritori(words):
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True
n = int(input())
words = []
for i in range(n):
    words.append(input())

if __name__ == '__main__':
    checkShiritori()