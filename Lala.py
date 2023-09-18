def is_valid_date(date_str):
    
    try:
        day, month, year = map(int, date_str.split('.'))
        
        # Проверка допустимости месяца
        if month < 1 or month > 12:
            return False
        
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        else:
            
            if year_1(year):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        
        
        if year < 1 or year > 9999:
            return False
        
        return True
    except ValueError:
        
        return False

date_str =input('Введите дату в формате DD.MM.YYYY: ')
year_1=(int(input('Введите год для проверки високосного: ')))
if (year_1 % 4 == 0 and year_1 % 100 != 0) or (year_1 % 400 == 0):
    print('True')
else:
    print('false')


if is_valid_date(date_str):
    print(f"{date_str} True")
else:
    print(f"{date_str} False")