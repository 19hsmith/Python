# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x [1][0] = 15
# print (x)

# students[0]["last_name"] = "Bryant"
# print(students)

# sports_directory["soccer"][0] = ("Andres")
# print(sports_directory)

# z[0]['y'] = 30
# print (z)
# def iterateDictionary(arr):
#      for i in range(len(arr)):
#         hold = ""
#         for k, v in arr[i].items():
#             hold += f"{k}, {v} "
#         print(hold)
       

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# def interateDictionary2(key_name,some_list):
#     for i in range(len(some_list)):
#         print(some_list[i][key_name])

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# interateDictionary2("first_name", students)
# interateDictionary2("last_name", students)




# def printInfo(some_dict):
#     for k,v in some_dict.items():
#         print(k,len(v))
#         for i in range(len(v)):
#             print(v[i])
       

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }






# printInfo(dojo)