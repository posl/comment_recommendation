def getProblemIndex(S):
    # 1st char in S is the index of the 1st char in the alphabet
    # 2nd char in S is the index of the 2nd char in the alphabet
    # 3rd char in S is the index of the 3rd char in the alphabet
    # etc.
    # 1st char is 1, 2nd char is 2, etc.
    # 1st char is A, 2nd char is B, etc.
    # 1st char is 1, 2nd char is 27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, 4th char is 27*27*27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, 4th char is 27*27*27, 5th char is 27*27*27*27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, 4th char is 27*27*27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, 4th char is 27*27*27, 5th char is 27*27*27*27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, 4th char is 27*27*27, 5th char is 27*27*27*27, 6th char is 27*27*27*27*27, etc.
    # 1st char is 1, 2nd char is 27, 3rd char is 27*27, 4th char is 27*27*27, 5th char is 27*27*27*27, 6th char is 27*27*27*27*27, 7
