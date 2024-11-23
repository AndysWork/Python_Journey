#\(BMI=kg/m^{2}\)
# Men: BMR = (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) + 5
# Women: BMR = (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) - 161 
# BMR=66.4730 + 13.7516 x weight in kg + 5.0033 x height in cm – 6.7550 x age in years. 
# In women, BMR=655.0955 + 9.5634 x weight in kg + 1.8496 x height in cm – 4.6756 x age in years
# Underweight: BMI is less than 18.5 
# Healthy weight: BMI is between 18.5 and 24.9 
# Overweight: BMI is between 25 and 29.9 
# Obesity - >30
# Sedentary - 1.2
# Lightly active -If you exercise lightly or play sports 1–3 days per week, your activity factor is 1.375. 
# Moderately active - If you exercise moderately or play sports 3–5 days per week, your activity factor is 1.55. 
# Very active - If you exercise hard every day or twice a day, your activity factor is 1.725. 
# Extra active - If you exercise very hard, train, or have a physical job, your activity factor is 1.9. 
# To calculate your total daily calorie needs (TDEE), TDEE = BMR x activity factor 
def menu():
    print('1. Check BMI ')
    print('2. Check BMI Rating ')
    print('3. Check BMR ')
    print('4. Daily Calorie Consumption Expectation ' )
    print('5. Check Targeted Daily Calorie Consumption Expectation ')
    print('6. Body Statistics Report ')

def check_bmr(gender, weight, height, age):
    bmr = 0.0
    if gender.lower() == 'm':
        bmr = float((10 * weight) + (6.25 * height) - (5 * age) + 5)
    elif gender.lower() == 'f':
        bmr = float((10 * weight) + (6.25 * height) - (5 * age) - 161)
    return bmr

def check_bmi(weight, height):
    h_in_mit = round(height/100)
    return round(weight/ h_in_mit ** 2)

def check_tdee(bmr, lifestyle_type):
    activity_multipliers = {
        'sedentary' : 1.2,
        'lightly active' : 1.375,
        'moderately active' : 1.55,
        'very active' : 1.725,
        'extra active' : 1.9
    }
    return bmr * activity_multipliers[lifestyle_type.lower()]

def check_daily_calories(gender, age, height, weight, target_weight, target_timeframe, lifestyle_type):
    bmr = check_bmr(gender, weight, height, age)
    tdee = check_tdee(bmr, lifestyle_type)
    weight_difference = weight - target_weight
    total_calorie_deficit = weight_difference * 7700
    daily_calorie_deficit = float(total_calorie_deficit / target_timeframe)
    
    return tdee - daily_calorie_deficit

def use_again():
    replay = input('Do you wnat to use the app again? Y/N')
    if replay.lower() == 'y':
        return True
    else: 
        return False

def main():
    print('Welcom to Fitness Journey!')
    name = input('Please enter your name - ')
    gender = input('What\'s your gender(M-Male/F-Female)? ')
    age = int(input('What is your age? - '))
    height = int(input('What is your height(in cm)? - '))
    weight = float(input('Would you like to tell us your weight(in kgs)? - '))
    target_weight = float(input('What\'s your target weight(in kgs)? - '))
    target_timeframe = int(input('What\'s timeframe you are looking for to achieve the target (in days)? - '))
    lifestyle_type = input('What\'s your lifestyle type (Sedentary, Lightly Active, Moderately Active, Very Active, Extra Active)? - ')
    choice = 0
    while True:
        menu()
        choice = int(input('Please enter your choice - '))
        if choice == 1:
            print('Your BMI is {}'.format(check_bmi(age, height)))
        elif choice == 2:
            bmi = check_bmi(weight, height)
            rating = ''
            if bmi < 18.5:
                rating = 'Underweight'
            elif bmi > 18.5 and bmi < 24.9:
                rating = 'Healthy Weight'
            elif bmi > 24.9 and bmi < 29.9:
                rating = 'Overweight'
            elif bmi > 29.9:
                rating = 'Obesity'
            print('Your BMI Rating is {}'.format(rating))
        elif choice == 3:
            bmr = check_bmr(gender, weight, height, age)
            print('Your BMR is {}'.format(bmr))
        elif choice == 4:
            tdee = check_tdee(check_bmr(gender, weight, height, age), lifestyle_type)
            print('Your Daily Calorie Consumption Expectation is {}'.format(tdee))
        elif choice == 5:
            target_daily_calories = check_daily_calories(gender, age, height, weight, target_weight, target_timeframe, lifestyle_type)
            print('Your targeted Daily Calorie Consumption will be {}'.format(target_daily_calories))
        elif choice == 6:
            bmr = check_bmr(gender, weight, height, age)
            tdee = check_tdee(bmr, lifestyle_type)
            daily_calories = check_daily_calories(gender, age, height, weight, target_weight, target_timeframe, lifestyle_type)
            report = f"""
            Body Statistics Report
            ----------------------
            Name - {name}
            Age - {age} Years
            Gender - {gender}
            Current Weight - {weight} Kg
            Target Weight - {target_weight} Kg
            Height - {height} cm
            Activity Level - {lifestyle_type}
            Target Timeframe - {target_timeframe} Days
            ---||||||||||---------|||||||||||--------
            Basal Metabolic Report (BMR) - {bmr: .2f} CAL/Day
            Total Daily Energy Expenditure (TDEE) - {tdee: .2f} CAL/Day
            Daily Calorie Intake to reach Target Weight - {daily_calories: .2f} CAL/Day
            """
            print(report)
        if not use_again:
            break
        
if __name__ == "__main__":
    main()