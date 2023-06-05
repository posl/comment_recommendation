def checkShiritori(words):
    if len(words) == len(set(words)):
        return True
    else:
        return False
