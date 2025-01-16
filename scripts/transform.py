import pandas as pd 

def clean_and_transform(data):
    # Replaces invalid data with NaN and removing missing rows
    data.replace('?', pd.NA, inplace=True)
    data.dropna(inplace=True)

    # Normalise the column names
    data.columns = data.columns.str.strip().str.lower().str.replace('/', '_')

    # Encodes categorical variables 
    data['gender'] = data['gender'].map({'m': 0, 'f': 1})
    data['class_asd'] = data['class_asd'].map({'NO': 0, 'YES': 1})

    #attempt at feature engineering
    data['age_group'] = pd.cut(data['age'], bins=[0,18,35,60,100],
                        labels=['Child', 'Young Adult', 'Adult', 'Senior'])
    data['family_history'] = data['autism'].map({'yes': 1, 'no': 0})
    return data

if __name__ == "__main__":
    data = pd.read_csv("autism_screening.csv")
    transformed_data = clean_and_transform(data)
    print(transformed_data.head())
