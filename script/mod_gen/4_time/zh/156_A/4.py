def get_inner_score(outer_score, num_of_contest):
    if num_of_contest < 10:
        return outer_score + 100 * (10 - num_of_contest)
    else:
        return outer_score

if __name__ == '__main__':
    get_inner_score()