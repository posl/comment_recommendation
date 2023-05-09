def is_substring(string, substring):
    for i in range(len(string)):
        if string[i] == substring[0]:
            if string[i:i+len(substring)] == substring:
                return True
    return False

if __name__ == '__main__':
    is_substring()