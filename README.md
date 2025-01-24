# Email Control Program

This project is an Email Control Program that allows users to send and receive emails using Python. It utilizes the `smtplib` and `imaplib` libraries to handle email operations.

## Features
- Send emails using SMTP.
- Receive and manage emails using IMAP.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chirag-sharma04/Email_control_program.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Email_control_program
   ```

3. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Email Control Program, you need to provide your email credentials. Here is an example of how to use the program:

```python
from email_control_program import EmailControl

email_user = 'your_email@example.com'
email_password = 'your_password'

email_control = EmailControl(email_user, email_password)
# Use the methods of EmailControl to send or receive emails
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License.
