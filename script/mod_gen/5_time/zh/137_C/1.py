def get_hash(text):
    hash = 0
    for i in range(len(text)):
        hash += ord(text[i]) * (i+1)
    return hash

if __name__ == '__main__':
    get_hash()