import pandas as pd

def load_data(file_path):
    # Load the dataset
    data = pd.read_csv("/data/autism_screening.csv")
    print(data.head()) #this allows you to preview the first few rows of the .csv
    print("Data loaded.")
    return data

if __name__ == "__main__":
    file_path = "/data/autism_screening.csv"
    raw_data = load_data(file_path)