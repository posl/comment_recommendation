def rotate(string):
    string = string[::-1]
    string = string.replace('6','a')
    string = string.replace('9','6')
    string = string.replace('a','9')
    return string

if __name__ == '__main__':
    rotate()