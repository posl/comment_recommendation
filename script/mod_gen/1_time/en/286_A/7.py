def swap(array, start, end):
    if start == end:
        return array
    else:
        return array[:start-1] + array[end-1:start-2:-1] + array[end:]

if __name__ == '__main__':
    swap()