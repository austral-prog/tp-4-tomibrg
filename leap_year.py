def leap_year():
    year = int(input('Ingrese un año: '))
    bisi_o_no_bisi = ''
    if (year % 100 == 0) and (year % 400 == 0):
        bisi_o_no_bisi = f'El año {year} es bisiesto'
    elif year % 4 == 0 and not(year % 100 == 0):
        bisi_o_no_bisi = f'El año {year} es bisiesto'
    else:
        bisi_o_no_bisi = f'El año {year} no es bisiesto'
    print(bisi_o_no_bisi)
leap_year()
