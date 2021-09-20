def find_avg(param1):
    newvar = len(param1)
    total = sum (param1)
    return total // newvar


tatyana_grades = [8,5,6,7,7,7,9,8]
brian_grades = [10,10,10,9,10,10,10,9]
nicole_grades = [9,8,9,8,8,9,7,9,8]

print(find_avg(tatyana_grades)) # should return 7
find_avg(brian_grades) # should return 9
find_avg(nicole_grades) # should return 8