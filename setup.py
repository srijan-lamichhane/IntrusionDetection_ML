from setuptools import setup, find_packages

setup(
    name='IntrusionVigor',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'joblib',
        'matplotlib',
        'seaborn',
        'setuptools',
        'notebook'
    ],
    entry_points={
        'console_scripts': [            
            'preprocess_data=scripts.01_preprocess_data:main',
            'train_scalar_model=scripts.02_train_scalar:main',
            'train_knn_model=scripts.03_train_knn:main',
            'train_random_forest_model=scripts.04_train_rf:main',
            'train_svm_model=scripts.05_train_svm:main',
            'train_gbm_model=scripts.06_train_gbm:main',
            'evaluate_knn_model=scripts.07_evaluate_model:evaluate_knn',
            'evaluate_random_forest_model=scripts.07_evaluate_model:evaluate_rf',
            'evaluate_svm_model=scripts.07_evaluate_model:evaluate_svm',
            'evaluate_gbm_model=scripts.07_evaluate_model:evaluate_gbm',
            'open_data_visualization_notebook=scripts.08_open_notebook:main',
            'main=main:main',   
        ],
    },
)
