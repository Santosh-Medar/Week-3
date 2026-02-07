import csv

#files to read
employeescsvfile="zenvy_employees.csv"
attendancecsvfile="zenvy_attendance.csv"

#file for output
outputcsvfile="zenvy_payroll.csv"

#constants
overtime_rate=350
tax_rate=0.10
pf_rate=0.05

#reading employee data
emps={}
with open(employeescsvfile,"r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        emps[row["employee_id"]]=row

#reading attendance data
attd={}
with open(attendancecsvfile,"r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        attd[row["employee_id"]]=row

#payroll calculation
payroll_list=[]
for emp_id in emps:
    emp=emps[emp_id]

    if emp_id not in attd:
        continue

    att=attd[emp_id]

    base_salary=float(emp["base_salary"])
    working_days=int(att["working_days"])
    present_days=int(att["present_days"])
    overtime_hours=float(att["overtime_hours"])
    per_day_salary=base_salary/working_days
    earned_salary=per_day_salary*present_days
    overtime_pay=overtime_hours*overtime_rate
    gross_salary=earned_salary+overtime_pay
    tax=gross_salary*tax_rate
    pf=gross_salary*pf_rate
    net_salary=gross_salary-(tax+pf)

    payroll_list.append({
        "employee_id":emp_id,
        "gross_salary":round(gross_salary, 2),
        "tax_deduction":round(tax, 2),
        "pf_deduction":round(pf, 2),
        "net_salary":round(net_salary, 2)
    })

#writing output file
with open(outputcsvfile,"w",newline="") as f:
    fieldnames=[
        "employee_id",
        "gross_salary",
        "tax_deduction",
        "pf_deduction",
        "net_salary"
    ]
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(payroll_list)

print("Payroll calculation completed. Output saved to", outputcsvfile)