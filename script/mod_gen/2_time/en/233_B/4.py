def reverse_string(string, left, right):
    return string[:left-1] + string[left-1:right][::-1] + string[right:]

if __name__ == '__main__':
    reverse_string()