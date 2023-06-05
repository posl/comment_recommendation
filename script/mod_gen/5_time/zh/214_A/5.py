def num_of_questions(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8

if __name__ == '__main__':
    num_of_questions()