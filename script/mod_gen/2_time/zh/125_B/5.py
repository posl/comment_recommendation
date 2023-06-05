def cookie_maker(a,b,t):
    cookie = 0
    for i in range(1,t+1):
        if i%a == 0:
            cookie += b
    return cookie

if __name__ == '__main__':
    cookie_maker()