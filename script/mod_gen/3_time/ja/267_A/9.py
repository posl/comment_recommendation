def get_ans(s):
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return 7 - day.index(s)

if __name__ == '__main__':
    get_ans()