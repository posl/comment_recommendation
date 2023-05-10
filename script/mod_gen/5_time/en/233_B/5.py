def reverse_string(string, start, end):
    string = string[:start-1] + string[start-1:end][::-1] + string[end:]
    return string

if __name__ == '__main__':
    reverse_string()