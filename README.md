# IntrusionVigor

IntrusionVigor is a machine learning-based intrusion detection system designed to preprocess data, train various models, and evaluate their performance. This project aims to enhance network security by leveraging advanced machine learning techniques.

## Table of Contents

- [IntrusionVigor](#intrusionvigor)
  - [Table of Contents](#table-of-contents)
  - [Project Abstract](#project-abstract)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Commands](#commands)
  - [Contributing](#contributing)
  - [License](#license)

## Project Abstract

IntrusionVigor aims to empower network security by utilizing machine learning algorithms for intrusion detection. The system preprocesses network data, trains multiple machine learning models including K-Nearest Neighbors, Random Forest, Support Vector Machine, and Gradient Boosting Machine, and evaluates their effectiveness. This project provides a user-friendly command-line interface to facilitate the preprocessing, training, and evaluation processes, making it easier to integrate and deploy advanced intrusion detection capabilities.

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.6 or higher
- Git

## Installation For Linux

Follow these steps to set up the project:

1. **Clone the repository**:
   ```zsh
   git clone https://github.com/srijan-lamichhane/IntrusionDetection_ML.git
   cd IntrusionVigor
   ```
2. **Copy the `.env.example` to `.env`**:
   ```zsh
    cp .env.example .env
   ```
3. **Create a virtual environment**:
   ```zsh
    python -m venv _venv
   ```
4. **Activate virtual environment `_venv` and `.env` file**:
    ```zsh
    source _venv/bin/activate
    source .env
    ```
5. **Install the required packages**:
    ```zsh
    pip install -r requirements.txt
    ```
6. **Install the package**:
    ```zsh
    python setup.py install
    ```

## Installation For Windows

1. **Clone the repository**:
   ```zsh
   git clone https://github.com/srijan-lamichhane/IntrusionDetection_ML.git
   cd IntrusionVigor
   ```

2. **Install virtual Environment**:
   ```zsh
    pip install virtualenv
   ```

3. **create virtual Environment**:
   ```zsh
    virtualenv venv
   ```

4. **Activate virtual Environment**:
   ```zsh
    venv/scripts/activate
   ```

5. **set PYTHONPATH environment variable**:
   ```zsh
   $env:PYTHONPATH = "$env:PYTHONPATH;$PWD"
   ```

6. **Install the required packages**:
    ```zsh
    pip install -r requirements.txt
    ```
7. **Install the package**:
    ```zsh
    python setup.py install
    ```



## Usage

Once the installation steps are completed, you can run the program using the following command:

```zsh
main
```

This will start the Intrusion Detection System menu where you can choose various options to preprocess data, train models, and evaluate them.

## Commands

Here are the available commands in the menu:

0. **Exit**: Exit the program.
1. **Preprocess Data**: Prepare the data for training.
2. **Train Scalar Model**: Train the scaler model for data normalization.
3. **Train KNN Model**: Train the K-Nearest Neighbors model.
4. **Train Random Forest Model**: Train the Random Forest model.
5. **Train SVM Model**: Train the Support Vector Machine model.
6. **Train GBM Model**: Train the Gradient Boosting Machine model.
7. **Evaluate KNN Model**: Evaluate the K-Nearest Neighbors model.
8. **Evaluate Random Forest Model**: Evaluate the Random Forest model.
9. **Evaluate SVM Model**: Evaluate the Support Vector Machine model.
10. **Evaluate GBM Model**: Evaluate the Gradient Boosting Machine model.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).                          