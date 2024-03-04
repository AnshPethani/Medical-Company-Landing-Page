from flask import Flask, request
import os

app = Flask(__name__)

# Function to append data to CSV file
def is_empty(file_path):
    return os.stat(file_path).st_size == 0

def append_to_csv(data):
    file = 'data.csv'

    if not os.path.isfile(file) or is_empty(file):
        with open(file, 'w') as f:
            f.write('Name,Email,Phone\n')  # Add header row if file is empty

    with open(file, 'a') as f:
        f.write(','.join(data) + '\n')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        form_data = [name, email, phone]

        # Append form data as a new row in the CSV file
        append_to_csv(form_data)

        return 'Form data added to CSV file successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)

