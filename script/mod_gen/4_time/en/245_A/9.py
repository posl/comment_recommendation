def get_time():
    time = input()
    time = time.split(' ')
    time = [int(i) for i in time]
    return time

if __name__ == '__main__':
    get_time()