# list comprehension => used when you want to create a new list from a list/string/range of numbers/etc., without a loop
# "key word" representation for list comprehension
# new_list = [new_item for item in list]

# conditional list comprehension
# new_list = [new_item for item in list if test]

numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)
# [2, 3, 4]

name = "Mirela"
new_list = [letter for letter in name]
print(new_list)
# ['M', 'i', 'r', 'e', 'l', 'a']

numbers_2 = [n * 2 for n in range(1, 5)]
# [2, 4, 6, 8]
names = ["mirela", "tibi", "petrica", "mami", "alexa"]
# ['mirela', 'tibi', 'petrica', 'mami', 'alexandra']
short_names = [name for name in names if len(name) < 5]
long_upper_names = [name.upper() for name in names if len(name) > 5]


# dictionary comprehension => create a new dict from the values in a list or a dictionary
# new_dict = {new_key: new_value for item in list}
# create a dictionary based on the values in an existing dictionary
# new_dict = {new_key: new_value for (key, value) in dict.items() + if test}

# import random
# students_scores = { student: random.randint(1, 100) for student in names}
# passed_students = {student: scores for (student, scores) in students_scores.items() if scores > 60}


# How to iterate over a Pandas DataFrame

students_dict = {
    "student": ["Mirela", "Tibi", "Petrica", "Mihai", "Elena"],
    "score": [89, 87, 96, 69, 58]
}
for (key, value) in students_dict.items():
    # print(key)
    print(value)

import pandas

student_df = pandas.DataFrame(students_dict)
print(student_df)

# Loop through a dataframe
# for (key, value) in student_df.items():
#     print(value)

# Loop through rows of a data frame
print("================================")
for (index, row) in student_df.iterrows():
    if row.student == "Mirela":
        print(row.score)
