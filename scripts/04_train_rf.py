from src.data.load_data import load_data
from src.models.random_forest import train_and_save_rf
from src.processing.scaler import load_scaler

def main():
    # Load preprocessed data and scaler
    train_df = load_data('data/processed/train_data_processed.csv')
    scaler = load_scaler('models/scaler.pkl')

    # Define features and labels
    X_train = train_df.drop(columns=['attack'])
    Y_train = train_df['attack']

    # Standardize features
    X_train = scaler.transform(X_train)

    # Train and save Random Forest model
    train_and_save_rf(X_train, Y_train, 'models/random_forest_model.pkl')

    # Print sucess message
    print('!!Random Forest Model Training Successful!! \n Check Random Forest Model at /models/')

if __name__ == '__main__':
    main()
