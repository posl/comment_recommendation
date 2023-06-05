def checkShiritori(words):
    if len(words) != len(set(words)):
        return False
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
    return True
n = int(input())
words = [input() for i in range(n)]

if __name__ == '__main__':
    checkShiritori()