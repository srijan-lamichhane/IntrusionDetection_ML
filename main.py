import subprocess

def main():
    menu_options = {
        1: 'Open Data Visualization Notebook',
        2: 'Preprocess Data',
        3: 'Train Scalar Model',
        4: 'Train KNN Model',
        5: 'Train Random Forest Model',
        6: 'Train SVM Model',
        7: 'Train GBM Model',
        8: 'Evaluate KNN Model',
        9: 'Evaluate Random Forest Model',
        10: 'Evaluate SVM Model',
        11: 'Evaluate GBM Model',
        0: 'Exit',
    }

    while True:
        print("\nIntrusionVigor: Empowering Network Security with Machine Learning - Main Menu")
        for key in sorted(menu_options.keys()):
            print(f"{key}. {menu_options[key]}")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue
        
        if choice == 0:
            print("Exiting the program.")
            break
        elif choice in menu_options:
            script_name = f"{menu_options[choice].lower().replace(' ', '_')}"
            print(script_name)
            if script_name != 'Exit':
                subprocess.run([script_name])
            else:
                print(f"Script {script_name} not found.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
        