import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_currency_amounts(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

# Example usage
if __name__ == "__main__":
    sample_text = """
        Contact me at user@example.com or visit https://example.com.
        My phone number is (123) 456-7890. 
        The price is $1,234.56.
        <div>Hello World</div>
    """
    
    print("Emails:", extract_emails(sample_text))
    print("URLs:", extract_urls(sample_text))
    print("Phone Numbers:", extract_phone_numbers(sample_text))
    print("Currency Amounts:", extract_currency_amounts(sample_text))
    print("HTML Tags:", extract_html_tags(sample_text))

