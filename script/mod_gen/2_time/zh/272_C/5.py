def check_meeting(meeting, n):
    for i in range(n):
        for j in range(n):
            if i != j and meeting[i][j] == 0:
                return False
    return True

if __name__ == '__main__':
    check_meeting()