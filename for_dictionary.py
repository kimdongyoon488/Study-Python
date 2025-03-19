person = {'name':'egoing', 'address':'Seoul'}
print(person['name'])

for key in person:
    print(key, person[key])

persons =[
{'name':'egoing', 'address':'Seoul'},
{'name':'basta', 'address':'Busan'}
] 

print('=== persons === ')
for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('---------')