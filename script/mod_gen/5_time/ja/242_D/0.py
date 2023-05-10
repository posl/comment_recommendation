def replaceABC(s):
    s = s.replace("A","BC")
    s = s.replace("B","CA")
    s = s.replace("C","AB")
    return s

if __name__ == '__main__':
    replaceABC()