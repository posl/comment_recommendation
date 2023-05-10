def get_anagram_count(input_list):
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if sorted(input_list[i]) == sorted(input_list[j]):
                anagram_count += 1
    return anagram_count

if __name__ == '__main__':
    get_anagram_count()