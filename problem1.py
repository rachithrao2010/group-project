def reverse(string):
    list = []
    for letter in string:
        list.append(letter)
    list.reverse()
    separator = ""
    new_string = separator.join(list)
    return new_string

