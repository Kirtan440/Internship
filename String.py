"""
print("Hey My name is: %s my roll no is : %d how are you: %s" % ('Kirtan',
51, 'I am fine'))
a = 10
b = "Rydham"
print(str(a) + b)
print("%s %d" % (b, a))
print('{},{}'.format(a, b))
"""


str_ex = 'Softvan_innoventa'
#print(str_ex)
# Softvan_innoventa

#print(str_ex[0])

#print(str_ex[2:7])

#print(str_ex[2:])

#print(str_ex * 2)

#print(str_ex + " Hello")
#print(str_ex, 'hello')
print(str_ex[0:5] + " " + str_ex[8:12])

#format method
print("My name is %s and I am from %s" %('Kirtan', 'Ahmedabad'))

"""
a = 10
b = "Rydham"
print(str(a) + b)
print("%s %d" % (b, a))
print('{},{}'.format(a, b))
"""

a = "Hello"
print(len(a))
print(a.capitalize())

#str= "This is the example of string"
#sub_str = "i"
#print(str.count(sub_str,3,30))

str1 = "This is the example of string"
str2 = "stri"
print(str1.find(str2))
print(str2.islower())

str3 = "THIS IS THE EXAMPLE OF UPPERCASE STRING"
print(str3.isupper())
print(str3.lower())

print(str3.replace("IS", "was"))

c = "55"
print(c.isdigit())

str4 = "  This is the example of string with spaces   "
reverse = str4[::-1]
print(reverse)

s = "this is string example"
reverse_words = ' '.join(reversed(s.split()))
print(reverse_words)
print(s.replace("is", "was"))

s1 = "this is string example"

s1 = s1.replace("i", "e")
print(s1)

words = s1.split()
result = '*'.join(words)
print(result)
print(s1.count('e'))

final = "this this is"
sub_str = "is"

result = final.replace("is","was")
print(result)