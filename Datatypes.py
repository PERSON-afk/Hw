String Examples

Single-quoted string

string1 = 'Hello'

Double-quoted string

string2 = "World"

Multi-line string

string3 = """This is a multi-line string."""

String Usage

Concatenation

greeting = string1 + ' ' + string2

Accessing elements

first_char = string1[0]  # 'H'

Slicing

substring = string1[1:4]  # 'ell'

Common Methods

uppercase = string1.upper()  # 'HELLO' lowercase = string2.lower()  # 'world'

List Examples

Defining a list

my_list = [1, 2, 3, 4, 5]

List Usage

Adding elements

my_list.append(6)  # [1, 2, 3, 4, 5, 6]

Accessing elements

first_item = my_list[0]  # 1

Slicing

sublist = my_list[1:3]  # [2, 3]

Common Methods

my_list.remove(2)  # Removes the first occurrence of 2 length = len(my_list)  # 5

Tuple Examples

Defining a tuple

my_tuple = (1, 2, 3)

Tuple Usage

Accessing elements

second_item = my_tuple[1]  # 2

Slicing

subtuple = my_tuple[0:2]  # (1, 2)

Tuple Unpacking

a, b, c = my_tuple  # a=1, b=2, c=3

Set Examples

Defining a set

my_set = {1, 2, 3}

Set Usage

Adding elements

my_set.add(4)  # {1, 2, 3, 4}

Removing elements

my_set.remove(2)  # {1, 3, 4}

Set operations

another_set = {3, 4, 5} union_set = my_set | another_set  # {1, 3, 4, 5} intersection_set = my_set & another_set  # {3, 4}

Dictionary Examples

Defining a dictionary

my_dict = {'key1': 'value1', 'key2': 'value2'}

Dictionary Usage

Accessing values

value1 = my_dict['key1']  # 'value1'

Adding or updating key-value pairs

my_dict['key3'] = 'value3'  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

Removing key-value pairs

del my_dict['key2']  # {'key1': 'value1', 'key3': 'value3'}

Iterating through keys and values

for key, value in my_dict.items(): print(key, value)

