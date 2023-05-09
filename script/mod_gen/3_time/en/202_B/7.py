def rotate(string):
    string = string[::-1]
    string = string.replace('0','*')
    string = string.replace('1','0')
    string = string.replace('*','1')
    string = string.replace('6','*')
    string = string.replace('8','6')
    string = string.replace('*','8')
    string = string.replace('9','*')
    string = string.replace('0','9')
    string = string.replace('*','0')
    return string
string = input()
print(rotate(string))

if __name__ == '__main__':
    rotate()