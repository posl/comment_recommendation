def find_last_occurence(string, char):
    index = -1
    for i in range(len(string)):
        if string[i] == char:
            index = i + 1
    return index
string = input()
char = 'a'
print(find_last_occurence(string, char))

if __name__ == '__main__':
    find_last_occurence()