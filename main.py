from location import get_location
from hospitals import get_nearest_hospitals
from symptoms import display_symptoms, get_symptoms

def get_patient_info():
    print("Please provide the following information:")
    name = input("Name: ").strip()
    gender = input("Gender (Male/Female/Other): ").strip()
    age = input("Age: ").strip()

    while not age.isdigit():
        print("Invalid age. Please enter a numeric value.")
        age = input("Age: ").strip()

    age = int(age)
    return name, gender, age

def get_symptom_severity(symptom):
    while True:
        try:
            severity = int(input(f"Rate the severity of your '{symptom}' on a scale of 1 (Low) to 5 (High): ").strip())
            if severity < 1 or severity > 5:
                raise ValueError
            return severity
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def is_sharp_and_continuous(symptom):
    response = input(f"Is the '{symptom}' sharp and continuous? (yes/no): ").strip().lower()
    return response == 'yes'

def calculate_emergency_score(symptom_details):
    critical_symptoms = {"Chest pain or discomfort", "Shortness of breath", "Feeling lightheaded or faint"}
    severity_score = sum(detail['severity'] for detail in symptom_details.values())
    sharp_and_continuous_score = sum(detail['sharp_and_continuous'] for detail in symptom_details.values())
    critical_symptoms_score = sum(1 for symptom in symptom_details if symptom in critical_symptoms)

    severity_score = (severity_score / (5 * len(symptom_details))) * 5
    sharp_and_continuous_score = (sharp_and_continuous_score / len(symptom_details)) * 3
    critical_symptoms_score = (critical_symptoms_score / len(critical_symptoms)) * 2

    total_score = severity_score + sharp_and_continuous_score + critical_symptoms_score
    return total_score

def display_symptom_details(symptom_details):
    print("\nSymptom Details:")
    for symptom, details in symptom_details.items():
        print(f"{symptom} - Severity: {details['severity']}, Sharp and Continuous: {'Yes' if details['sharp_and_continuous'] else 'No'}")

def display_emergency_message(score):
    print(f"\nTotal Emergency Score: {score:.2f}")
    if score > 7:
        print("This is an emergency. Rush to the hospital immediately!")
    elif score > 5:
        print("Seek medical attention as soon as possible!")
    else:
        print("Contact your doctor or seek medical assistance if symptoms persist.")

def display_nearby_hospitals(hospitals):
    print("\nNearby Hospitals:")
    for hospital in hospitals:
        print(f"Name: {hospital['name']}")
        print(f"Address: {hospital['address']}")
        print(f"Coordinates: {hospital['coordinates'][0]}, {hospital['coordinates'][1]}")
        print()

if __name__ == "__main__":
    name, gender, age = get_patient_info()

    print(f"\nPatient Information:\nName: {name}\nGender: {gender}\nAge: {age}")

    symptoms = get_symptoms()
    display_symptoms()

    selected_symptoms = input("\nPlease select the symptoms you are experiencing (enter the numbers separated by commas): ")
    selected_symptoms_indices = [int(i.strip()) - 1 for i in selected_symptoms.split(',')]

    symptom_details = {}
    for i in selected_symptoms_indices:
        symptom = symptoms[i]
        severity = get_symptom_severity(symptom)
        sharp_and_continuous = is_sharp_and_continuous(symptom)
        symptom_details[symptom] = {
            'severity': severity,
            'sharp_and_continuous': sharp_and_continuous
        }

    display_symptom_details(symptom_details)
    emergency_score = calculate_emergency_score(symptom_details)
    display_emergency_message(emergency_score)
    
    if emergency_score > 7:
        print("\nFetching nearby hospitals...")
        try:
            user_location = get_location()
            hospitals = get_nearest_hospitals(user_location)
            if hospitals:
                display_nearby_hospitals(hospitals)
            else:
                print("No nearby hospitals found.")
        except Exception as e:
            print(f"An error occurred while fetching nearby hospitals: {e}")
        
        print("\nPlease call the emergency number 112 (or 100) immediately.")
