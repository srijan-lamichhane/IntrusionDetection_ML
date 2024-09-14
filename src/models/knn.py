from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import joblib

def train_and_save_knn(X_train, Y_train, model_path):
    """Train and save the KNN model."""
    param_grid = { ... }  # Use the param_grid as provided earlier
    grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, verbose=2)
    grid.fit(X_train, Y_train)
    joblib.dump(grid.best_estimator_, model_path)

def load_knn(model_path):
    """Load the KNN model."""
    return joblib.load(model_path)
