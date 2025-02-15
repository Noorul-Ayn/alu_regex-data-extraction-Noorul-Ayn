# alu_regex-data-extraction-Noorul-Ayn

## Overview
This project demonstrates regex-based data extraction from a sample text. The code extracts various data types such as:

- Email addresses
- URLs
- Phone numbers
- Currency amounts
- HTML tags

The `extract_data.py` script utilizes regular expressions to identify and extract these data types from a string. The extracted data is then displayed on the console.

## Project Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Noorul-Ayn/alu_regex-data-extraction-Noorul-Ayn.git
   cd alu_regex-data-extraction-Noorul-Ayn

2. Navigate to the project directory:
cd alu_regex-data-extraction-Noorul-Ayn

3. Run the script:
python3 extract_data.py

##EXAMPLE USAGE

sample_text = """
    Contact me at user@example.com or visit https://example.com.
    My phone number is (123) 456-7890.
    The price is $1,234.56.
    <div>Hello World</div>

When the script runs, it will extract the following:

Emails: ['user@example.com']
URLs: ['https://example.com']
Phone Numbers: ['(123) 456-7890']
Currency Amounts: ['$1,234.56']
HTML Tags: ['<div>Hello World</div>']

##Conclusion:
That's pretty much it. Thank you!
"""




