def rotate_string(str):
    str = str[::-1]
    str = str.replace("0", "a")
    str = str.replace("1", "b")
    str = str.replace("6", "0")
    str = str.replace("9", "1")
    str = str.replace("a", "6")
    str = str.replace("b", "9")
    return str
