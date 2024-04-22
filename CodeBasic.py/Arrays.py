expenses =[
    { "January":2200},
    { "February": 2350},
    {"March": 2600},
    {"April": 2130},
    {"May": 2190}
      
    ]

compare_months = expenses[1]["February"] - expenses[0]["January"] 
expense_months= expenses[1]["February"] + expenses[0]["January"] + expenses[2]["March"]



for ex in expenses:
    if ex == 2600:
        print(ex)



expenses.append( {"June": 1980})
# print (expenses)

expenses.pop(3)
expenses.insert(3,{"April": 1930})
# print (expenses)
# print(expense_months)

heros=['spider man','thor','hulk','iron man','captain america']

length = len(heros)

print(length)

heros.insert(3, 'black panther')

print(heros)

heros[1:3]= ['doctor strange']

print(heros)

heros.sort()

print( heros)


max= int(input("enter max number:"))
odd_list = []

for i in range(1, max):
    if i % 2 == 1:
        odd_list.append(i)

    print (odd_list)

