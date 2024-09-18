from calendar import month

month_birth = str(input(
    'Введите месяц вашего рождения (январь/февраль/март/апрель/май/июнь/июль/август/сентябрь/октябрь/ноябрь/декабрь): '))
data_birth = int(input('Введите дату вашего рождения : '))
if (month_birth == 'декабрь' and data_birth >= 22) or (month_birth == 'январь' and data_birth <= 20):
    print('козерог')
elif (month_birth == 'январь' and data_birth >= 21) or (month_birth == 'февраль' and data_birth <= 18):
    print('водолей')
elif (month_birth == 'февраль' and data_birth > 18) or (month_birth == 'март' and data_birth <= 20):
    print('рыбы')
elif (month_birth == 'март' and data_birth >= 21) or (month_birth == 'апрель' and data_birth <= 19):
    print('овен')
elif (month_birth == 'апрель' and data_birth >= 20) or (month_birth == 'май' and data_birth <= 20):
    print('телец')
elif (month_birth == 'май' and data_birth >= 21) or (month_birth == 'июнь' and data_birth <= 21):
    print('близнецы')
elif (month_birth == 'июнь' and data_birth >= 22) or (month_birth == 'июль' and data_birth <= 21):
    print('рак')
elif (month_birth == 'июль' and data_birth >= 22) or (month_birth == 'август' and data_birth <= 22):
    print('лев')
elif (month_birth == 'август' and data_birth >= 23) or (month_birth == 'сентябрь' and data_birth <= 22):
    print('дева')
elif (month_birth == 'сентябрь' and data_birth >= 23) or (month_birth == 'октябрь' and data_birth <= 23):
    print('весы')
elif (month_birth == 'октябрь' and data_birth >= 24) or (month_birth == 'ноябрь' and data_birth <= 22):
    print('скорпион')
elif (month_birth == 'ноябрь' and data_birth > 22) or (month_birth == 'декабрь' and data_birth <= 21):
    print('стрелец')
