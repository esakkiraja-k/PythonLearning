employee_file = open("employees.txt","r")
print(employee_file.readable())
for employee in employee_file.readlines():
    print(employee)
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines())
employee_file.close()

#open("employees.txt","w")
#open("employees.txt","r+") read/write
#open("employees.txt","a") append
