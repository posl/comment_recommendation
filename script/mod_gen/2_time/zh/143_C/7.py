def merge_slime(slime):
    if len(slime) == 1:
        return 1
    else:
        return merge_slime(slime[1:]) + 1

if __name__ == '__main__':
    merge_slime()