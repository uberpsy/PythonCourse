def validate_name(name):
    return True if len(name) >= 2 else False


def validate_height(height):
    return True if 50 <= height <= 250 else False


def validate_weight(weight):
    return True if 5 <= weight <= 300 else False


def get_user_data():
    while True:
        name = input("Enter your name: ")
        if validate_name(name):
            break
    while True:
        weight = int(input("Enter weight in kilograms: "))
        if validate_weight(weight):
            break
    while True:
        height = int(input("Enter height in centimeters: "))
        if validate_height(height):
            break
    return {"name": name, "height": height, "weight": weight}


def calc_BMI(w, h):
    return w / (h * h)


def calc_BMI_category(bmi):
    if bmi < 16:
        category = "Underweight (Severe thinness)"
    elif 16 <= bmi <= 16.9:
        category = "Underweight (Moderate thinness)"
    elif 17 <= bmi <= 18.4:
        category = "Underweight (Mild thinness)"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal range"
    elif 25 <= bmi <= 29.9:
        category = "Overweight (Pre-obese)"
    elif 30 <= bmi <= 34.9:
        category = "Obese (Class I)"
    elif 35 <= bmi <= 39.9:
        category = "Obese (Class II)"
    else:
        category = "Obese (Class III)"

    return category


def print_results(bmi_category):
    print(f"Your BMI category is {bmi_category}")


def cm_to_meters(cm):
    return float(cm / 100)


user_data = get_user_data()
height_in_meters = cm_to_meters(user_data["height"])
bmi = calc_BMI(user_data["weight"], height_in_meters)
bmi_category = calc_BMI_category(bmi)
print_results(bmi_category)
