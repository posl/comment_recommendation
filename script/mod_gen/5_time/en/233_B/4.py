def reverse_string(string, start, end):
    return string[:start-1] + string[start-1:end][::-1] + string[end:]

if __name__ == '__main__':
    reverse_string()