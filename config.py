from datetime import date
import json

colonia_ferias = False
feriados = ['2019-01-01',
            '2019-04-21',
            '2019-05-01',
            '2019-09-07',
            '2019-09-20',
            '2019-10-12',
            '2019-11-02',
            '2019-11-15',
            '2019-12-25']

if not colonia_ferias:
    dias_aula = range(1,7)
else:
    dias_aula = range(0,6)

# terça a sábado
if date.today().isoformat() not in feriados and \
date.today().weekday() in dias_aula:
    #abre o json e atribui à data
    with open('calendar.json', 'r') as calendar:
        data = json.load(calendar)

    if data['verde']:
        data['verde'] = False
    else:
        data['verde'] = True

    #salva
    with open('calendar.json', 'w') as calendar:
        calendar.write(json.dumps(data, indent=4))
