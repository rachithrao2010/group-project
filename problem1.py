def reverse(string):
    list = []
    for letter in string:
        list.append(letter)
    list.reverse()
    separator = ""
    new_string = separator.join(list)
    return new_string

print(reverse("Hello"))
print(reverse("Encyclopedia"))
print(reverse("Table"))
print(reverse("Wall-e"))
print(reverse("speaker"))
