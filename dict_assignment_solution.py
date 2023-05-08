
company = {
    'departments': {
        'HR': {
            'employees': {
                'employee_1': {
                    'name': 'John Doe',
                    'position': 'HR Manager',
                    'salary': 60000
                },
                'employee_2': {
                    'name': 'Jane Smith',
                    'position': 'HR Assistant',
                    'salary': 45000
                }
            },
            'policies': ['recruitment', 'onboarding', 'benefits']
        },
        'IT': {
            'employees': {
                'employee_3': {
                    'name': 'Alice Brown',
                    'position': 'IT Manager',
                    'salary': 70000
                },
                'employee_4': {
                    'name': 'Bob Johnson',
                    'position': 'Software Developer',
                    'salary': 65000
                }
            },
            'projects': ['website', 'intranet', 'software development']
        },
        'Finance': {
            'employees': {
                'employee_5': {
                    'name': 'Charlie White',
                    'position': 'Finance Manager',
                    'salary': 68000
                },
                'employee_6': {
                    'name': 'Eva Green',
                    'position': 'Accountant',
                    'salary': 55000
                }
            },
            'budgets': ['operations', 'marketing', 'research']
        }
    },
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zipcode': '12345'
    },
    'founders': ['Emily Williams', 'Oliver Taylor'],
    'year_founded': 2000
}





#Q1
emp_3 = company["departments"]["IT"]["employees"]["employee_3"]["name"]
print(f"The name of the third emplyee in the IT department is {emp_3}.\n")

#Q2
e,f,g = company["departments"]["HR"]["policies"]
print(f"The policies of the HR department are {e}, {f} and {g}.")
print('\n')

#Q3
emps = []
for i in company["departments"].keys():
  for j in company["departments"][i]["employees"]:
    emps.append(j)

emp_total = len(emps)
print(f"There are {emp_total} employees in the company.\n")

#Q4
emp_salary = []
tot_sal = 0
for i in company['departments'].keys():
  for j in company['departments'][i]['employees'].keys():
    emp_salary.append(company['departments'][i]['employees'][j]['salary'])

for salary in emp_salary:
  tot_sal += salary

avg_sal = tot_sal / len(emp_salary)

print(f"The average employee salary is ${avg_sal:.2f}\n")


#Q5
a,b,c = company['departments']['IT']['projects']
print(f"The IT department is working on {a}, {b} and {c}.")
print('\n')


#Q6
x,y = company['founders']
print(f"The founders of the company are {x} and {y}.")
print('\n')


#Q7
p,q,r,s = company['address']['street'], company['address']['city'], company['address']['state'], company['address']['zipcode']
print(f"The address of the company is\n{p},\n{q},\n{r},\n{s}.")
print('\n')


#Q8
emp_names = []
emp_sals = []

for i in company['departments'].keys():
  for j in company['departments'][i]['employees'].keys():
    emp_names.append(company['departments'][i]['employees'][j]['name'])
    emp_sals.append(company['departments'][i]['employees'][j]['salary'])

for i,j in zip(emp_names,emp_sals):
  if j == max(emp_sals):
    print(f"{i} is the highest paid employee with salary of ${j}")
  else:
    continue  
print("\n")

#Q9
depts = []
emp_num = []
for i in company['departments'].keys():
  depts.append(i)
  emp_num.append(len(company['departments'][i]['employees']))

for i,j in zip(depts, emp_num):
  print(f"{i} department has {j} employees")
print("\n")
print("There are equal numbers of employees in the departments.")
print("\n")


#Q10
emp_name = []
emp_post = []

for i in company['departments']['Finance']['employees']:
  emp_name.append(company['departments']['Finance']['employees'][i]['name'])
  emp_post.append(company['departments']['Finance']['employees'][i]['position'])


for i,j in zip(emp_name,emp_post):
  print(f"{i} is the {j} for the Finance department.")
print('\n')