def extra_users_followed():
    data = input('Enter the number of users following you and the number of users you are following: ')
    data = data.split()
    a = int(data[0])
    b = int(data[1])
    return 2 * a + 100 - b
print(extra_users_followed())
