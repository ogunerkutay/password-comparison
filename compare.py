import csv
import argparse

def read_password_data(file_path):
    """Reads password data from a CSV file into a dictionary, normalizing keys."""
    data = {}
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Adjust if the column names are different
                if 'url' in row and 'username' in row and 'password' in row:
                    # Normalize the key for more robust, case-insensitive comparison.
                    # This treats 'User' and 'user' as the same.
                    # It also removes leading/trailing whitespace.
                    norm_url = row['url'].lower().strip()
                    norm_username = row['username'].lower().strip()
                    key = (norm_url, norm_username)
                    
                    # If a normalized key already exists, we have a potential duplicate within the same file.
                    # For this comparison, we'll let the last entry win.
                    data[key] = row['password']
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")
        print("Please ensure the CSV file has 'url', 'username', and 'password' columns.")
        raise
    return data

def compare_csv_files(file1, file2):
    """
    Compares two CSV files and finds conflicts.
    A conflict is defined as the same url and username having different passwords.
    Also reports entries unique to each file.
    """
    data1 = read_password_data(file1)
    data2 = read_password_data(file2)

    conflicts = []
    for key, password in data1.items():
        if key in data2 and data2[key] != password:
            conflicts.append({
                'url': key[0],
                'username': key[1],
                'password_file1': password,
                'password_file2': data2[key]
            })

    unique_to_file1 = []
    for key in data1:
        if key not in data2:
            unique_to_file1.append({
                'url': key[0],
                'username': key[1],
                'password': data1[key]
            })
    
    unique_to_file2 = []
    for key in data2:
        if key not in data1:
            unique_to_file2.append({
                'url': key[0],
                'username': key[1],
                'password': data2[key]
            })

    if conflicts:
        print("--- Conflicts (same url and username, different password) ---")
        for conflict in conflicts:
            print(f"URL: {conflict['url']}, Username: {conflict['username']}")
            print(f"  Password in {file1}: {conflict['password_file1']}")
            print(f"  Password in {file2}: {conflict['password_file2']}")
        print("\n")

    if unique_to_file1:
        print(f"--- Unique entries in {file1} ---")
        for item in unique_to_file1:
            print(f"URL: {item['url']}, Username: {item['username']}, Password: {item['password']}")
        print("\n")

    if unique_to_file2:
        print(f"--- Unique entries in {file2} ---")
        for item in unique_to_file2:
            print(f"URL: {item['url']}, Username: {item['username']}, Password: {item['password']}")
        print("\n")
    
    if not conflicts and not unique_to_file1 and not unique_to_file2:
        print("No conflicts or differences found between the two files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two password CSV files for conflicts and differences.")
    parser.add_argument("file1", help="Path to the first CSV file (e.g., 'Chrome Passwords.csv')")
    parser.add_argument("file2", help="Path to the second CSV file (e.g., 'Microsoft Edge Passwords.csv')")
    args = parser.parse_args()

    try:
        compare_csv_files(args.file1, args.file2)
    except Exception:
        # The specific error is already printed in the read_password_data function
        print("Comparison could not be completed due to an error.")