# String Examples

string1 = 'Hello'
string2 = "World"
string3 = """This is a multi-line string."""

# String Usage

greeting = string1 + ' ' + string2
first_char = string1[0]
substring = string1[1:4]
uppercase = string1.upper()
lowercase = string2.lower()

# List Examples

my_list = [1, 2, 3, 4, 5]

# List Usage

my_list.append(6)
first_item = my_list[0]
sublist = my_list[1:3]
my_list.remove(2)
length = len(my_list)

# Tuple Examples

my_tuple = (1, 2, 3)

# Tuple Usage

second_item = my_tuple[1]
subtuple = my_tuple[0:2]
a, b, c = my_tuple

# Set Examples

my_set = {1, 2, 3}

# Set Usage

my_set.add(4)
my_set.remove(2)
another_set = {3, 4, 5}
union_set = my_set | another_set
intersection_set = my_set & another_set

# Dictionary Examples

my_dict = {'key1': 'value1', 'key2': 'value2'}

# Dictionary Usage

value1 = my_dict['key1']
my_dict['key3'] = 'value3'
del my_dict['key2']
for key, value in my_dict.items():
    print(key, value)
