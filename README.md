# Cyber URL Scanner

Cyber URL Scanner is a web-based security tool designed to analyze and detect potential threats associated with a given URL. It checks for suspicious activities, SSL status, and domain details.

## Features
- Scan URLs for phishing activity
- Fetch IP address and SSL certificate status
- Get domain information like registrar and country
- User-friendly UI for displaying scan results

## Installation
### Prerequisites
- Python 3.x
- Django

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/cyber-url-scanner.git
   cd cyber-url-scanner
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Django server:
   ```sh
   python manage.py runserver
   ```
5. Open your browser and go to:
   ```sh
   http://127.0.0.1:8000/
   ```

## API Integration (Currently Not Used)
This project includes code for integrating APIs such as:
- **Google Safe Browsing API** for threat detection
- **WHOIS API** for domain lookup
- **IPInfo API** for IP address details

However, these APIs are not currently in use. Instead, sample data is used to simulate results.

## Usage
1. Enter a URL in the scanner input field.
2. Click the "Scan" button.
3. View the scan results including status, IP address, SSL details, and domain information.

## Contributing
Feel free to submit pull requests or report issues.

## License
This project is licensed under the MIT License.
