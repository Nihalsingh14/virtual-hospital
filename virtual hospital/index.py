# Cell 1: Data injection cell (will be replaced with form data)
data = {}

# Cell 2: Disease symptom matching logic
diseases_symptoms = {
    "Common Cold": ["cough", "sore throat", "runny nose", "congestion"],
    "Flu": ["fever", "chills", "muscle aches", "cough", "congestion", "runny nose", "fatigue"],
    "COVID-19": ["fever", "dry cough", "tiredness", "loss of taste or smell"],
    "Strep Throat": ["sore throat", "painful swallowing", "fever", "red and swollen tonsils"],
    "Allergies": ["sneezing", "runny nose", "itchy eyes", "congestion", "cough"],
    # Add more diseases and their symptoms here
}

matched_diseases = []
for disease, symptoms in diseases_symptoms.items():
    if any(symptom in data.values() for symptom in symptoms):
        matched_diseases.append(disease)

# Cell 3: Output the matched diseases
matched_diseases
