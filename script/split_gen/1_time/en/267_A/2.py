def main():
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    S = input()
    print(week.index('Saturday') - week.index(S) + 1)
