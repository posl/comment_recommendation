def str2int(str):
    int = 0
    for s in str:
        int = int * 26 + ord(s) - ord('a')
    return int
