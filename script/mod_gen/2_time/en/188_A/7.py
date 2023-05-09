def check_score(X, Y):
    if X > Y:
        if (X - Y) < 3:
            return "No"
        else:
            return "Yes"
    else:
        if (Y - X) < 3:
            return "No"
        else:
            return "Yes"

if __name__ == '__main__':
    check_score()