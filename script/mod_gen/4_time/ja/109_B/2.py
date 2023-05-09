def check_shiritori(words):
    if len(words) == len(set(words)):
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                return False
        return True
    else:
        return False
N = int(input())
words = [input() for _ in range(N)]

if __name__ == '__main__':
    check_shiritori()