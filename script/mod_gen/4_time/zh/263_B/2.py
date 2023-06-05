def get_father(person):
    father = 0
    if person == 1:
        father = 0
    else:
        father = p[person-2]
    return father

if __name__ == '__main__':
    get_father()