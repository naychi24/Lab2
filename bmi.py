def calculate_bmi(height, weight): 
    print("height " + str(height))
    print("weight " + str(weight))
    bmi = weight / (height ** 2)
    print("bmi " + str(bmi))

    if bmi < 18.5:
        classification = -1
    elif 18.5 <= bmi <= 25:
        classification = 0
    else:
        classification = 1

    return bmi, classification

def classify_bmi(bmi_value):
    if bmi_value < 18.5:
        print("Underweight")
    elif 18.5 <= bmi_value <= 25:
        print("Normal weight")
    else: 
        print("Overweight")
    return

def app():
    bmi, class_value = calculate_bmi(1.7, 60)
    classify_bmi(bmi)
    print("Classification value:", class_value)
    return

if __name__ == "__main__":
    app()

