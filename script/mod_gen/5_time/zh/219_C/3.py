def get_key_index(key):
    key_index = [0]*26
    for i in range(len(key)):
        key_index[ord(key[i])-97] = i
    return key_index

if __name__ == '__main__':
    get_key_index()