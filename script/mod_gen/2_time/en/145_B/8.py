def is_concatenation_of_two_copies(s):
    if len(s) % 2 == 0:
        t = s[:int(len(s)/2)]
        if s == t + t:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

if __name__ == '__main__':
    is_concatenation_of_two_copies()