def replace_comma(string):
    #print(string)
    string = list(string)
    #print(string)
    #print(len(string))
    #print(string.count('"'))
    #print(string.count(','))
    #print(string.count('"')/2)
    #print(string.count(',')/2)
    #print(string.count('"')/2 - string.count(',')/2)
    #print(int(string.count('"')/2 - string.count(',')/2))
    for i in range(int(string.count('"')/2 - string.count(',')/2)):
        #print(i)
        #print(string.index('"'))
        string[string.index('"')] = '.'
        #print(string)
        string.pop(string.index('"'))
        #print(string)
        string.pop(string.index('"'))
        #print(string)
    return ''.join(string)

if __name__ == '__main__':
    replace_comma()