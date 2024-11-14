import csv

def read_profiles_from_csv(input_filename):
    """Read LinkedIn profile URLs from a CSV file and return them as a list."""
    profiles = []
    with open(input_filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            profiles.append(row[0])  # Assuming URLs are in the first column
    return profiles

def save_to_csv(data, output_filename="linkedin_emails.csv"):
    """Save profile URL and email data to a CSV file."""
    with open(output_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
