def calculate_age(birth_year, current_year):
    result =   birth_year - current_year 
    return result
    
birth_year  = int(input())

current_year = 2025


print(calculate_age(birth_year,current_year))