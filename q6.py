def to_print(hour, min, type):

    hour_setup = type + ".M"

    print(str(hour) + ":" + str(min) + " " + hour_setup)

def convert_time(hour, min):

    if(hour <= 12 and hour > 0):

        return to_print(hour, min, "A")

    elif hour != 0:
        return to_print(hour-12, min, "P")
    
    else:
        return to_print(12, min, "P")

continue_convert = str(input("Deseja realizar uma operação? (s/n): ").upper())


while(continue_convert == 'S'):

    hour = int(input("Hora: "))
    min = int(input("Minutos: "))

    convert_time(hour, min)

    continue_convert = str(input("Deseja realizar outra operação? (s/n): ").upper())


