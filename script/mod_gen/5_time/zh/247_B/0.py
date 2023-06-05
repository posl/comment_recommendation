def get_nickname(n):
    nicknames = []
    for i in range(n):
        nicknames.append(input().split(' '))
    return nicknames

if __name__ == '__main__':
    get_nickname()