# def first_non_repeating(string: str):
#     for char in string:
#         if string.count(char) == 1:
#             return char

# def first_non_repeating(string: str):
#     dict = {}
#     for char in string:
#         count = dict.get(char, 0)
#         dict[char] = count + 1
#     print(dict)
#     for key in dict:
#         if dict[key] == 1:
#             return key

def first_repeating(string: str):
    _set = set()
    for char in string:
        if char in _set:
            return char
        _set.add(char)


print(first_repeating("a greenppleg"))

print(1+int("a"))
