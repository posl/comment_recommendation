def check_attendees(attendees):
    for i in range(len(attendees)):
        for j in range(i+1,len(attendees)):
            if attendees[i] == attendees[j]:
                return True
    return False

if __name__ == '__main__':
    check_attendees()