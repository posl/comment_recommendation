def judge(year,month,day):
    if year < 2019:
        return True
    elif year > 2019:
        return False
    else:
        if month < 4:
            return True
        elif month > 4:
            return False
        else:
            if day <= 30:
                return True
            else:
                return False

if __name__ == '__main__':
    judge()