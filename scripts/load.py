import pandas as pd

#saves the cleaned data to a database
def save_data(data, file_path):
    data.to.csv(file_path, index=False)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    data = pd.read_csv("cleaned_autism_screening.csv")
    save_data(data, "final_autism_data.csv")
