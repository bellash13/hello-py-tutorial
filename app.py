citizens = []
leave = False
totalMale = 0
totalFemale = 0

while True and not leave:
    name = input("Enter citizen name: ")

    gender = input("Is citizen male (M) or female(F): ")
    if gender == 'M':
        totalMale += 1
    elif gender == 'F':
        totalFemale += 1
    else:
        print('Invalide gender. Use F for female or M for male')
        continue

    age = int(input("How old is the citizen: "))

    citizen = {name:name, gender:gender, age: age}

    citizens.append(citizen)
    
    choice = input("Stop adding citizen? Yes(Y) or No (N)")
    
    leave = choice == 'Y'

print(f"Total male: {totalMale} total female {totalFemale}")
