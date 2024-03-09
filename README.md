### Messaging-Bot For Messages for web

**Bulk Number Adder** is a Python application that uses ChromeDriver to automatically add contact numbers in bulk from a CSV file to a specified platform.

#### How it Works:

1. **Setup Environment:**
   - Ensure you have Python installed on your system.
   - Download the appropriate ChromeDriver version for your Chrome browser.

2. **Install Dependencies:**
   - Use `pip` to install the required Python packages:
     ```
     pip install selenium
     ```

3. **Prepare CSV File:**
   - Create a CSV file with contact numbers as the only column.

4. **Configure the Application:**
   - Open the `config.py` file and update the `CSV_FILE_PATH` variable with the path to your CSV file.

5. **Run the Application:**
   - Execute the `bulk_number_adder.py` script.
     ```
     python bulk_number_adder.py
     ```

6. **Automated Process:**
   - The application will launch a Chrome browser window.
   - It will read the contact numbers from the CSV file.
   - It will automatically add the numbers to the specified platform, up to a maximum of 100 numbers.

7. **Verify Results:**
   - Once the process is complete, verify that the numbers have been successfully added to the platform.

#### Screenshots:

[Add screenshots here]
