def checkShiritori(words):
    if len(words) == len(set(words)):
        return True
    else:
        return False

if __name__ == '__main__':
    checkShiritori()