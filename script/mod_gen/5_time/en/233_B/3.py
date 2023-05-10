def reverse_string(string, start, stop):
    if start == 0:
        return string[stop::-1] + string[stop+1:]
    else:
        return string[:start-1] + string[stop:start-2:-1] + string[stop+1:]

if __name__ == '__main__':
    reverse_string()