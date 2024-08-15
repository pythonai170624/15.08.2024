info_dict: dict = {
    "name": "oren",
    "age": 31,
    "id": "74829302",
    "height": 1.98,
    "smoker": False,
    "brothers_age": [18, 20],
    "grades": (80, 99, 100),
    "address": {"city": "tel-aviv", "street": "ben-yehuda", "number": 12}
}
print(info_dict)
info_dict['age'] = 29  # if not exist -> create. if exist -- update
info_dict['weight'] = 85
print(info_dict)
print(info_dict['height'])
#print(info_dict[0])  # looks for key 0
#print(info_dict['does not exist'])  # Error if key not exist
print(info_dict.get(0))  # None
print(info_dict.get(0, '0 does not exist'))

print(tuple(info_dict.keys()))
print(list(info_dict.keys()))
print(tuple(k for k in info_dict.keys() if k != 'id'))

print(tuple(v for v in info_dict.values() if not isinstance(v, tuple)))

print(tuple(info_dict.items()))

print(dict(tuple(info_dict.items())))

x, y = 1, 2  # x=1 y=2
x, y = (1, 2)  # x=1 y=2
x, y = [1, 2]  # x=1 y=2
# a=1 b=2 c=3 d=4
a, b, c, d = 1, 2, 3, 4

list_pairs: list[int] = [[1, 2], [3, 4], [5, 6], [7, 8]]
for item in list_pairs:
    left: int = item[0]
    right: int = item[1]
    left, right = item[0], item[1]
    #print(f"{left},{right}")
    print('item', item)
for item in list_pairs:
    left, right = item[0], item[1]
for left, right in list_pairs:  # both (0, [1, 2])
    print(f"left is {left}, right is {right}")
for both in enumerate(list_pairs):
    print('both', both)
for index, item in enumerate(list_pairs):
    left = item[0]
    right = item[1]
    print(index, item)
for index, (left, right) in enumerate(list_pairs):
    print(f"index: {index} left: {left}, right: {right}")


print([item for item in info_dict.items()])
for item in info_dict.items():
    print(f"[{item[0]}]: {item[1]}")
for key, value in info_dict.items():
    print(f"[{key}]: {value}")

numbers: list[int] = [80, 90, 10, 1, -200, 10, 10]
for index, number in enumerate(numbers):
    print(f"{index}: {number}")
    if index > 0 and numbers[index - 1] == number:
        print('two equal sequence numbers')

for index, item in enumerate(list_pairs):
    (left, right) = item
    print(f"{index}: left-{left} right-{right}")

#                        0       1       2       3
list_pairs: list[int] = [[1, 2], [3, 4], [5, 6], [7, 8]]
#            item
for index, (left, right) in enumerate(list_pairs):
    # [left, right] = item
    print(f"{index}: left-{left} right-{right}")

left, right = (1, 2)
left, right = [1, 2]
(left, right) = [1, 2]
[left, right] = [1, 2]

info_dict.clear()
print('clear', info_dict)

info_dict = {"name": "oren", "age": 31, "height": 1.98, "smoker": False, "brothers_age": [18, 20],\
             "address": {"city": "tel-aviv", "street": "ben-yehuda", "number": 12}}

info_copy = info_dict.copy()
print('copy', info_copy)

print('from keys 1', dict.fromkeys(['name', 'smoker'], None))
print('from keys 2', dict.fromkeys(info_dict.keys(), None))

print('get name', info_dict.get('name'))
print('get weight', info_dict.get('weight', 0))

print('pop name', info_dict.pop('name'))
print('after pop name', info_dict)

print('pop item', info_dict.popitem())  # remove last item
print('after pop item', info_dict)

customers = {1: {'name': 'oren', 'age': 31}, 2: {}, 12873: {'name': 'robocop'}}
print(customers.get(12873))

info_dict['name'] = 'danny'
d1 = {'a': 1, 'b': 2}
d2 = {'c': 1, 'd': 2, b: 3}
d1.update(d2)
info_dict.update({"name": "danny", "age": 18})
print('after update', info_dict)

info_dict['name'] = 'moshe'  # [key]
print('after update', info_dict)

del info_dict['name']
print('after delete', info_dict)
try:
    del info_dict['name']
except:
    print('could not delete. does it exist?')

dict_books = dict([[1, "1984"], [3, "Harry potter"], [5, "Game of thrones"]])
dict_books = dict([(1, "1984"), (3, "Harry potter"), (5, "Game of thrones")])
print('dict() function ', dict_books)
print('get len', len(dict_books))
print('str dict', str(dict_books))
db_dict: dict = {True: {"name": "shalom", "age": 20}, 2: {}}
print(db_dict)


# dictionary with 1 lambda function
def add_two(x, y):
    return x + y

oper_dict0: dict = {"+": add_two}
print(oper_dict0.get("+")(1, 3))  # 4

# dictionary with 4 lambda function
# --- Extra ---
oper_dict: dict = {"+": add_two, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}
print(add_two(1, 3))
print(oper_dict["+"](1, 3))
# if oper == "+":
#     add_two(1, 3)
# elif oper == "-":
#     min(1, 3)
"""
x: int = int(input("enter x: "))
y: int = int(input("enter y: "))
oper: str = input("enter oper: ")  # + - * /
# result = oper_dict.get(oper)(x, y)
# print(f"{x} {oper} {y} = {result}")

# run all operations
for k in oper_dict.keys():
    result = oper_dict[k](x, y)
    print(f"{x} {k} {y} = {result}")
"""

square_dict = {}
for x in range(1, 10):
    square_dict[x] = x ** 2
print(square_dict)
square_dict_short = dict((x, x**2) for x in range(1, 10))  # dict((1, 1), (2, 4))
square_dict_short = {x: x**2 for x in range(1, 10)}  # dict((1, 1), (2, 4))
print(square_dict_short)

list1 = [2, 3, 7, 9, 10, 15, 30]
if_dict = {item: item**2 for item in list1 if item % 2 == 0}
print(if_dict)

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4, 5, 6, 7]
print(dict(zip(keys, values)))

