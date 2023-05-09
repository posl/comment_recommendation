def main():
    input_string = input()
    if input_string[0] == input_string[1] and input_string[1] == input_string[2]:
        print('Bad')
    elif input_string[1] == input_string[2] and input_string[2] == input_string[3]:
        print('Bad')
    else:
        print('Good')
