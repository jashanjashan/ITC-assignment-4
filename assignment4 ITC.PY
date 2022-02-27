#q1
def tower_of_hanoi(n,from_disk,to_disk,middle_disk):
    if n==0:
            return
    tower_of_hanoi(n-1,from_disk,middle_disk,to_disk)
    print(f"move Disk {n} from {from_disk} to  {to_disk}")
    tower_of_hanoi(n-1,middle_disk,to_disk,from_disk)

tower_of_hanoi(3,"A","B","C")

#q2
print("using recursion")
def func(n):
    for i in range(n+1):
        for j in range(n-i):
            print(' ',end='')
        x=1
        for j in range(1,i+1):
            print(x," ",sep=' ',end=' ')
            x=x*(i-j)//j
        print()
n=int(input("enter no: "))
func(n)

print("using iteration")
from math import factorial
for i in range(n):
    for j in range(n-i+1):
        print(' ',end="")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)),' ',end=' ')
    print()

#q3
print("a part")
number1=int(input("enter a no"))
number2=int(input("enter the second no"))
y=[number2,number2]
def function(a,b):
    x=divmod(a,b)
    return x

print(callable(function))
#q3(b)
print("B part")
values=function(number1,number2)
print(values)
if all([v!=0 for v in values]):
    print("they are none zero")
else:
    print("not all are simultaneously non zero")

#q3(C)
print("C part")
my_list=list(values)
my_list.extend([4,5,6])
list_upto_4=[1,2,3,4]
   

list_of_filtered_values=filter(lambda x:x>4,my_list)
filtered_values=tuple(list_of_filtered_values)
print(filtered_values)

#q3(d)
print("D part")
set_required=set(values)
print(set_required)

#q3(e)
print("E part")
immutable_set=frozenset(set_required)
print(immutable_set)

#q3(f)
print("F part")
max_value=max(set_required)
print("max_value",max_value)
hash_value=hash(immutable_set)
print("hash_value",hash_value)


#q4
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def __del__ (self):
        print("object is destroyed")
student_data=Student("Jashan",21103087)
print(student_data.name)
print(student_data.roll_number)

print("now call the del function and destroy object")
del(student_data)
# if we print the student data it will throw an error
print(student_data)

#q5
print("a part")
class employees:
    def __init__(self,Employee,Name,Salary):
        self.Employee=Employee
        self.Name=Name
        self.Salary=Salary
employee_1=employees(1,"Mehak",40000)
employee_2=employees(2,"Ashok",50000)
employee_3=employees(3,"Viren",60000)
present_salary_of_Mehak=employee_1.Salary
present_salary_of_Mehak=70000
update_salary_of_Mehak=present_salary_of_Mehak
print("updated salary of Mehak",update_salary_of_Mehak)
print("DONE!")

print("B part")
del employee_3
print(employee_3,Salary)


#q6
word_spoken_by_George=input("words spoken by George: ")
def anagrams(string_entered_by_user):
    if string_entered_by_user==word_spoken_by_George[-1]:
        return [string_entered_by_user]
    else:
        ans=[]
        for i in anagrams(string_entered_by_user[1:]):
            for pos in range(len(i)+1):
                 ans.append(i[:pos]+string_entered_by_user[0]+i[pos:])
        return ans
#here u denotes word spoken by Barbie
u=anagrams(word_spoken_by_George)
print(u)





















        



        

    
        
    


