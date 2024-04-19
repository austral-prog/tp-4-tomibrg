def leap_year():
    year = int(input('Ingrese un año: '))
    is_leap_year_msg = ''
    
    if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and not(year % 100 == 0)):
         is_leap_year_msg = f'El año {year} es bisiesto'
     else:
         is_leap_year_msg = f'El año {year} no es bisiesto'
     print(is_leap_year_msg)
leap_year()
#    if (year % 100 == 0) and (year % 400 == 0):
#        is_leap_year_msg = f'El año {year} es bisiesto'
#    elif year % 4 == 0 and not(year % 100 == 0):
#        is_leap_year_msg = f'El año {year} es bisiesto'
#    else:
#        is_leap_year_msg = f'El año {year} no es bisiesto'
#    print(is_leap_year_msg)


