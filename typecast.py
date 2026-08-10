#type casting = the process of converting a value of one data type to another
#    string, integer, float, boolean
#    explicit vs implicit

gender = "gooding"
body_count = 89
hours = 1.2
student = True


# explicit ( manually converting the value of variable into another

print(type(gender))
print(type(body_count))
print(type(student))
print(type(hours))

# integer to float

body_count = float(body_count)
print (type(body_count))
print(body_count)

#float to integer
hours = int(hours)
print(hours)

#boolean to str
student = str(student)
print(student)

#integers to boolean
body_cout =bool(body_count)
print(body_cout)

 #implicit ( automatically coverting variables to another data type )

m = 4
n = 2.00

m = m / n
print(m)

