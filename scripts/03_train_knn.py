from src.data.load_data import load_data
from src.models.knn import train_and_save_knn
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

    # Train and save KNN model
    best_model, best_params = train_and_save_knn(X_train, Y_train, 'models/knn_model.pkl')

    print("Best Parameters:", best_params)
    
    # Print sucess message
    print('!!KNN Model Training Successful!! \n Check KNN Model at /models/')

if __name__ == '__main__':
    main()
