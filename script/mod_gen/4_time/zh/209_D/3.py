def get_father(n, father):
    if father[n] == n:
        return n
    else:
        return get_father(father[n], father)

if __name__ == '__main__':
    get_father()