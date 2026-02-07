# Zenvy Payroll Automation – Week 3

It reads employee details and attendance data from CSV files, calculates salary, and generates a payroll report.

## Input Files
- zenvy_employees.csv
- zenvy_attendance.csv

## Output File
- zenvy_payroll.csv

## Salary Logic
- Gross Salary = Earned Salary + Overtime Pay 
- Net Salary = Gross − (Tax + PF)
- Tax = 10% of Gross Salary  (Assumption) 
- PF = 5% of Gross Salary (Assumption) 

## How to Run
1. Keep all files in one folder  
2. Run: Python index.py 
3. Payroll CSV will be generated automatically

## Tools Used
- Python
- CSV module

