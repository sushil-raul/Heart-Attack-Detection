# symptoms.py

# List of common heart attack symptoms
heart_attack_symptoms = [
    "Chest pain or discomfort",
    "Shortness of breath",
    "Nausea or vomiting",
    "Pain in one or both arms",
    "Pain in the back, neck, or jaw",
    "Feeling lightheaded or faint",
    "Cold sweat",
    "Unusual fatigue"
]

def get_symptoms():
    """Returns the list of heart attack symptoms."""
    return heart_attack_symptoms

def display_symptoms():
    """Prints the list of heart attack symptoms."""
    print("Heart Attack Symptoms:")
    for index, symptom in enumerate(heart_attack_symptoms, 1):
        print(f"{index}. {symptom}")

if __name__ == "__main__":
    display_symptoms()
