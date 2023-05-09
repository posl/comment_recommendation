def find_missing_element():
    # Get the list of input strings
    input_list = []
    for i in range(3):
        input_list.append(input())
    # Define the list of all the 4 contest series
    contest_series = ['ABC', 'ARC', 'AGC', 'AHC']
    # Find the missing element
    for i in range(3):
        for j in range(4):
            if input_list[i] == contest_series[j]:
                contest_series[j] = ''
    for i in range(4):
        if contest_series[i] != '':
            print(contest_series[i])
find_missing_element()

if __name__ == '__main__':
    find_missing_element()