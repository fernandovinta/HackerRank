def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        tempString = string[i:]
        if tempString[:len(sub_string)] == sub_string:
            count = count + 1
    return count
