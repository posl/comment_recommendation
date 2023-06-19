def follow(a,b):
    if a in follow_dic:
        if b in follow_dic[a]:
            return True
    return False

if __name__ == '__main__':
    follow()