def find_father(fathers, x):
    if fathers[x] == x:
        return x
    else:
        fathers[x] = find_father(fathers, fathers[x])
        return fathers[x]

if __name__ == '__main__':
    find_father()