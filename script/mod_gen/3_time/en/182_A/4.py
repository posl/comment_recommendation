def get_followers():
    followers = input().split()
    return int(followers[0]), int(followers[1])

if __name__ == '__main__':
    get_followers()