import os
import json


def evaluate_entities(file_name, data):

    entities = data
    total = len(entities)

    # Initialize error counters
    assertion_errors = {"POSITIVE": 0, "NEGATIVE": 0, "UNCERTAIN": 0}
    temporality_errors = {"CURRENT": 0, "CLINICAL_HISTORY": 0, "UPCOMING": 0, "UNCERTAIN": 0}
    subject_errors = {"PATIENT": 0, "FAMILY_MEMBER": 0}

    missing_attributes = 0
    date_correct = 0

    for e in entities:

        entity_type = e.get("entity_type")
        assertion = e.get("assertion")
        temporality = e.get("temporality")
        subject = e.get("subject")

        text = e.get("text", "").lower()

        # Assertion rule example
        if assertion == "POSITIVE" and "denies" in text:
            assertion_errors["POSITIVE"] += 1

        # Temporality rule example
        if temporality == "CURRENT" and "history of" in text:
            temporality_errors["CURRENT"] += 1

        # Subject rule example
        if subject == "PATIENT" and any(x in text for x in ["father", "mother", "family history"]):
            subject_errors["PATIENT"] += 1

        # Metadata completeness check
        metadata = e.get("metadata_from_qa", {})

        if not metadata:
            missing_attributes += 1

        relations = metadata.get("relations", [])

        for r in relations:
            if r.get("entity_type") == "derived_date":
                date_correct += 1

    result = {

        "file_name": file_name,

        "entity_type_error_rate": {
            "MEDICINE": 0.0,
            "PROBLEM": 0.0,
            "PROCEDURE": 0.0,
            "TEST": 0.0,
            "VITAL_NAME": 0.0,
            "IMMUNIZATION": 0.0,
            "MEDICAL_DEVICE": 0.0,
            "MENTAL_STATUS": 0.0,
            "SDOH": 0.0,
            "SOCIAL_HISTORY": 0.0
        },

        "assertion_error_rate": {
            k: (v / total if total else 0) for k, v in assertion_errors.items()
        },

        "temporality_error_rate": {
            k: (v / total if total else 0) for k, v in temporality_errors.items()
        },

        "subject_error_rate": {
            k: (v / total if total else 0) for k, v in subject_errors.items()
        },

        "event_date_accuracy": (date_correct / total if total else 0),

        "attribute_completeness": (1 - (missing_attributes / total) if total else 0)
    }

    return result


def process_dataset(dataset_path, output_path):

    for folder_name in os.listdir(dataset_path):

        folder_path = os.path.join(dataset_path, folder_name)

        if os.path.isdir(folder_path):

            for file_name in os.listdir(folder_path):

                if file_name.endswith(".json"):

                    json_file_path = os.path.join(folder_path, file_name)

                    with open(json_file_path, "r") as f:
                        data = json.load(f)

                    result = evaluate_entities(file_name, data)

                    output_file = os.path.join(output_path, file_name)

                    with open(output_file, "w") as f:
                        json.dump(result, f, indent=4)

                    print(f"Processed {file_name}")


if __name__ == "__main__":

    dataset_path = "/content/drive/MyDrive/workshop_test_data"
    output_path = "/content/output"

    os.makedirs(output_path, exist_ok=True)

    process_dataset(dataset_path, output_path)

    print("Evaluation complete.")