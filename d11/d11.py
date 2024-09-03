students_marks={
"anand":92,
"akhil":84,
"benison": 74,
"cenoy":64,
"hafeed": 55,
"jithin":42,
"nithin":28
}
'''
students_grades={}
for name in students_marks:
    mark=students_marks[name]
    #mark=students_marks.get(name)
    if mark>90:
        students_grades[name]="A+"
        # students_grades.update({name: 'A+'})
    elif mark>80:
            students_grades[name]="A"
    elif mark>60:
        students_grades[name]="B"
    elif mark>50:
        students_grades[name]="C"
    elif mark>40:
        students_grades[name]="D"
    elif mark>30:
        students_grades[name]="E"
    else:
        students_grades[name]="F"
print(students_grades)

#-------------------------------------------------------------------------
'''
#string methods
#--------------


#capitalize()
#-----------
text="good morning\n"
text2=text.capitalize()
print(text2)

#upper()
#-----------
text="good morning\n"
text2=text.upper()
print(text2)

#lower()
#-----------
text="good morning\n"
text2=text.lower()
print(text2)

#swapcase()
#-----------
text="good morning\n"
text2=text.swapcase()
print(text2)

#count()
#-----------
x="good morning good morning good morning"
print(x.count("good"))
print(x.count("good",0,40))
'''
#find()
#------
x="good morning"
print(x.find("good"))
print(find("good",15))

'''
#split()and join
#---------------
x="good morning"
print(x.split())

x="good$morning"
print(x.split('$'))
y=x.split('$') #list
y.append("six")
print(y)

x="$".join(y) # seperator.join(list)
print(x)


z="good$morning"
i=z.split('$')
z='\n'.join(i)
print(z)




s="""Twinkle, twinkle, little star

How I wonder what you are

Up above the world so high

Like a diamond in the sky

Twinkle, twinkle little star

How I wonder what you are

When the blazing sun is gone

When he nothing shines upon

Then you show your little light

Twinkle, twinkle, all the night
"""

t=s.split("/n")
print(t)

t.append("codeme")
s="\n".join(t)
print(s)

#splitlines()
#------------
c=s.splitlines()
print(c)


