journal = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
ABC = sorted(students)
journal = {
    ABC[0]: (float(sum(grades[0])) / len(grades[0])),
    ABC[1]: (float(sum(grades[1])) / len(grades[1])),
    ABC[2]: (float(sum(grades[2])) / len(grades[2])),
    ABC[3]: (float(sum(grades[3])) / len(grades[3])),
    ABC[4]: (float(sum(grades[4])) / len(grades[4]))
}
print(journal)