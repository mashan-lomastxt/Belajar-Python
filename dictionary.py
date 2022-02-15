# contoh membuat Dictionary pada Python
dict = {'Name': 'Zara', 'Age': 17, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# update dict pada python
dict = {'Name': 'Zara', 'Age': 17, 'Class': 'First'}
dict['Age'] = 18; # update value Age
dict['School'] = "DPS School"; # add new item

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# hapus dictionary pada python
dict = {"Name": "Zara", "Age": 17, "Class": "First"}

del dict["Name"] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict        # delete entire dictionary

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])