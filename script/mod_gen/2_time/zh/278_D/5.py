def follow(followers, followings, a, b):
    if a == b:
        return False
    if b in followings[a]:
        return True
    return False

if __name__ == '__main__':
    follow()