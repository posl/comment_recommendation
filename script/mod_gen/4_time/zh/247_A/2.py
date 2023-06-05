def changeStatus(status):
    status = list(status)
    if status[0] == '1':
        status[0] = '0'
    else:
        status[0] = '1'
    return ''.join(status)
status = input()
print(changeStatus(status))
