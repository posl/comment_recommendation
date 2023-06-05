def get_pronunciation_of_ben(num):
    if num[-1] == '2' or num[-1] == '4' or num[-1] == '5' or num[-1] == '7' or num[-1] == '9':
        return 'hon'
    elif num[-1] == '0' or num[-1] == '1' or num[-1] == '6' or num[-1] == '8':
        return 'pon'
    elif num[-1] == '3':
        return 'bon'
