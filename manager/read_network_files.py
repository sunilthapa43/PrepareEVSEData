from config import EVSE_NETWORK_PATH, OUTPUT_PATH
import os
import pandas as pd

# Define the directory containing your files and the output file path
directory = EVSE_NETWORK_PATH
output_dir = OUTPUT_PATH

# Adjusted list of attack scenarios to match exact patterns in filenames
attack_scenarios = [
    "portscan", "service-detection", "os-fingerprinting", "aggressive-scan",
    "syn-stealth", "vulnerability-scan", "slowloris-scan", "udp-flood", "icmp-flood",
    "pshack-flood", "icmp-fragmentation", "tcp-flood", "syn-flood", "synonymous-ip",
    "cryptojacking", "backdoor"
]

# List to collect all dataframes
dataframes = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file is a CSV file
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        # Convert to lowercase for consistent matching
        filename_lower = filename.lower()

        # Read the file into a DataFrame
        df = pd.read_csv(file_path, low_memory=False)

        # Initialize default values for each column
        state = "idle" if "idle" in filename_lower else "charging"
        label = "benign" if "benign" in filename_lower else "attack"
        if "benign" in filename_lower:
            scenario = "benign"
        else:
            # Determine the scenario based on the adjusted attack names
            scenario = next((attack for attack in attack_scenarios if attack in filename_lower), None)

        # Add new columns with the extracted values
        df['State'] = state.title()
        df['Scenario'] = scenario.replace("-", " ").title()  # Formatting for readability
        df['Label'] = label.title()

        # Append the modified DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
consolidated_df = pd.concat(dataframes, ignore_index=True)

output_file = OUTPUT_PATH + "network_data_combined.csv"
# Save the consolidated DataFrame to a single CSV file
consolidated_df.to_csv(output_file, index=False)

print(f"Consolidated data saved to {output_file}.")
