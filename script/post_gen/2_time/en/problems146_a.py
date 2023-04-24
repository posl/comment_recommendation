Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    days = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}
    print(days[input()])

=======
Suggestion 2

def main():
    S = input()
    if S == 'SUN':
        print(7)
    elif S == 'MON':
        print(6)
    elif S == 'TUE':
        print(5)
    elif S == 'WED':
        print(4)
    elif S == 'THU':
        print(3)
    elif S == 'FRI':
        print(2)
    elif S == 'SAT':
        print(1)

main()

=======
Suggestion 3

def main():
    day = input()
    if day == "SAT":
        print(1)
    elif day == "SUN":
        print(7)
    elif day == "MON":
        print(6)
    elif day == "TUE":
        print(5)
    elif day == "WED":
        print(4)
    elif day == "THU":
        print(3)
    elif day == "FRI":
        print(2)

=======
Suggestion 4

def main():
    S = input()
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    print(7 - days.index(S))

=======
Suggestion 5

def main():
    S = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(7 - days.index(S))

=======
Suggestion 6

def main():
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - days.index(s))

=======
Suggestion 7

def main():
    d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - d.index(s))

=======
Suggestion 8

def main():
    print(7 - ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"].index(input()))

=======
Suggestion 9

def main():
    # Write your code here
    weekday = input()
    if weekday == 'SUN':
        print('7')
    elif weekday == 'MON':
        print('6')
    elif weekday == 'TUE':
        print('5')
    elif weekday == 'WED':
        print('4')
    elif weekday == 'THU':
        print('3')
    elif weekday == 'FRI':
        print('2')
    else:
        print('1')

=======
Suggestion 10

def main():
    # Read the input
    S = input()
    
    # Convert the string to integer
    S = S.upper()
    if S == "SUN":
        S = 0
    elif S == "MON":
        S = 1
    elif S == "TUE":
        S = 2
    elif S == "WED":
        S = 3
    elif S == "THU":
        S = 4
    elif S == "FRI":
        S = 5
    elif S == "SAT":
        S = 6
    
    # Calculate the number of days to Sunday
    days = 7 - S
    
    # Print the result
    print(days)
