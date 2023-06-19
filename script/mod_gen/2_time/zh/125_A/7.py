def get_cookies(a,b,t):
    cookies = 0
    for i in range(1,t+1):
        if i % a == 0:
            cookies += b
    return cookies

if __name__ == '__main__':
    get_cookies()