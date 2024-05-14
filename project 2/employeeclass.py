''' Employee Management Database'''
class Empolyeemanger:
    ''''
    Represents an employee with their basic details and employment information.'''
   
    def __init__(self,employee_name:str,job_title:str,department:str,salary:float,hire_year:int):
        self.employee_name= employee_name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hireyear = hire_year
        if salary <= 0:
            raise ValueError("Salary must be greater than zero. ")
        if hire_year <1900 or hire_year > 2024:
            raise ValueError("Hire year ust be a realistic year.")
        
        # add new employee data
        employee = {'employee_name':employee_name,
                    'job_title':job_title , 'department': department, 'salary':salary, 'hire_year' : hire_year}
        self.employees.append(employee)
        return (f"Name: {self._name}, Job Title: {self._job_title}, "
                f"Department: {self._department}, Salary: ${self._salary}, "
                f"Hire Year: {self._hire_year}")

    def years_worked(self) -> int:
        """
        Calculates the number of years the employee has worked from the hire year to the current year.
        
        Returns:
            int: Number of years worked.
        """
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self._hire_year

    def total_expense(self) -> float:
        
        
        return self._salary * self.years_worked()

     # Accessor methods
    def get_name(self) -> str:
        
        return self._name
    
    def get_job_title(self) -> str:
        
        return self._job_title

    def get_department(self) -> str:
       
        return self._department
    
    def get_salary(self) -> float:
       
        return self._salary
    
    def get_hire_year(self) -> int:
       
        return self._hire_year

    # Mutator methods
    def set_name(self, name: str):
       
        self._name = name
    
    def set_job_title(self, job_title: str):
      
        self._job_title = job_title

    def set_department(self, department: str):
       
        self._department = department
    
    def set_salary(self, salary: float):
        
        self._salary = salary
    
    def set_hire_year(self, hire_year: int):
       
        self._hire_year = hire_year

# Example usage (commented out):
emp = Employee("John Doe", "Software Engineer", "Technology", 85000.0, 2018)
print(emp)
print(f"Years Worked: {emp.years_worked()}")
print(f"Total Expense: ${emp.total_expense():,.2f}")






     





