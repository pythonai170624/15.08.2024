import random
import statistics
from datetime import datetime, timedelta

group_max: tuple[int] = (100,)
print(group_max[0])
# group_max[0] += 1  # Error -- not allowed!

def do_not_change(list1: list[int]) -> None:
    list1.clear()

my_list = [1, 2, 3]
do_not_change(my_list)
print(my_list)

# do_not_change((1, 2, 3))  # Data integrity

simple_tuple: tuple[int] = (1, 2, 3)
one_item_tuple: tuple[int] = (1,)

fruits: tuple[str] = ("apple", "banana", "cherry")
print(fruits)
print(fruits[0])

mix: tuple[any] = (1, "Hello", [1, 2, 3], {"name": "danny"})
print(mix)
mix[2][0] = 100
mix[2].append(200)
print(mix)
tuple_tuples: tuple[tuple[int]] = ((0,), (), (1, 2, 3), "danny")
item_2 = tuple_tuples[2]  # (1, 2, 3)
#item_2[0] = 1  # Error
item_2 = "hello"
print(tuple_tuples)

#unpack
number_tuple: tuple[int] = (1, 2, 3)
x, y, z = number_tuple  # x=1 y=2 z=3
x = 10  # no problem

def get_add_mul(x: int, y: int) -> tuple[int]:
    return (x + y, x * y)
print(get_add_mul(2, 3))

create_tuple = tuple([1, 2, 3])  # create from list
print(create_tuple)
create_tuple_comp = tuple(x**2 for x in range(1, 6))  # create from list
print(create_tuple_comp)
create_nested_tuple: tuple[tuple[any]] = (
    ("Alice", 21, "Physics"),
    ("Bob", 222, "Chemistry"),
    ("Charlie", 20, "Mathematics")
)
print(create_nested_tuple)

names: tuple[str] = ("Alice", "Bob", "Charlie")
scores: tuple[int] = (80, 90, 99, 100)
combines_tuple: tuple[tuple[any]] = tuple(zip(names, scores))
print(combines_tuple)
list_combined = list(zip(names, scores))
print(list_combined)

numbers: tuple[int] = (1, 2, 0, 3, 2, 100)
print(numbers.count(2))
print(numbers.index(100))
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(statistics.mean(numbers))
print(sum(numbers))
print(any(numbers))
print(all(numbers))
sorted_tuple = tuple(sorted(numbers))
print(sorted_tuple)

tuple_1 : tuple[int] = (1, 2)
tuple_2 : tuple[int] = (3, 4)
print(tuple_1 + tuple_2)
print(tuple_1 * 3)
print(3 in tuple_2)

# 1
# create a tuple with numbers from 0-20
print(tuple(range(21)))
# 2
# tuple1 = 10 random numbers between 1-10 (1, 4, 5, 7)
# tuple2 = 10 random numbers between 1-10 (7, 2, 4, 6)
# tuple3 = only similar numbers            (4, 7)
# tuple(x for x in tuple1 if x in tuple2)
# Bonus: tuple3 should be unique ... without -- (2, 4, 2, .. )
tuple1: tuple[int] = tuple(random.randint(1, 10) for _ in range(10))
tuple2: tuple[int] = tuple(random.randint(1, 10) for _ in range(10))
tuple3: tuple[int] = tuple(x for x in tuple1 if x in tuple2)
print(tuple1)
print(tuple2)
print('both', tuple3)
# 2.5
# map each item from tuple 3 to it's square ==> i.e. 3 will become 9 in the new tuple
print(tuple(x**2 for x in tuple3))
# 3
# put in tuple the datetime.now and the next 7 days
# from datetime import datetime, timedelta
# print((datetime.now() + timedelta(days=1)).strftime("%H:%M:%S.%f %Y-%B-%d %A"))
print(tuple((datetime.now() + timedelta(days=x)).strftime("%H:%M:%S.%f %Y-%B-%d %A") for x in range(8)))
# 4
grades = (("Alice", 92), ("Bob", 90), ("Charlie", 88), ("David", 85), ("Eve", 79))
# create a new tuple of these pairs sorted by grades
print(tuple(sorted(grades, key=lambda pair: pair[1])))



