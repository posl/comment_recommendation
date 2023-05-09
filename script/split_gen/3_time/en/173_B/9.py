def main():
    # Get number of test cases
    numTestCases = int(input())
    # Initialize counters for each verdict
    ac = 0
    wa = 0
    tle = 0
    re = 0
    # Loop through the test cases
    for i in range(0,numTestCases):
        # Get the verdict
        verdict = input()
        # Increment the counter for the corresponding verdict
        if verdict == "AC":
            ac += 1
        elif verdict == "WA":
            wa += 1
        elif verdict == "TLE":
            tle += 1
        elif verdict == "RE":
            re += 1
    # Print the results
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))
