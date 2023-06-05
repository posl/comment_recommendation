def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return int(stepper * number) / stepper

if __name__ == '__main__':
    truncate()