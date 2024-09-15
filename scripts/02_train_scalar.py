from src.data.load_data import load_data
from src.processing.scaler import train_and_save_scaler

def main():
    # Load preprocessed data
    train_df = load_data('data/processed/train_data_processed.csv')

    # Define features
    X_train = train_df.drop(columns=['attack'])

    # Train and save the scaler
    train_and_save_scaler(X_train, 'models/scaler.pkl')

    # Print sucess message
    print('!!Scalar Model Training Successful!! \n Check Scalar Model at /models/')

if __name__ == '__main__':
    main()
