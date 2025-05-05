import random
import smtplib

def generate_otp():
    return random.randint(100000, 999999)

def send_email(receiver_email, otp, name):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        password = "xdfk dkft tmei pgoy"  # Replace with your App Password
        server.login("mr.zouraiz1580@gmail.com", password)

        subject = "OTP Verification"
        body = f"Dear {name},\n\nYour OTP is: {otp}\nPlease do not share it with anyone."
        message = f"Subject:{subject}\n\n{body}"

        server.sendmail("mr.zouraiz1580@gmail.com", receiver_email, message)
        server.quit()
        print(f"\nOTP has been sent to {receiver_email} 📧")
        return True
    except Exception as e:
        print(f"\n❌ Error sending email: {e}")
        return False

def email_verification(email):
    allowed_domains = ["gmail", "hotmail", "yahoo", "outlook"]
    allowed_extensions = [".com", ".in", ".org", ".edu", ".co.in"]

    if "@" not in email:
        return False
    domain_part = email.split("@")[1]

    domain_valid = any(domain in domain_part for domain in allowed_domains)
    extension_valid = any(email.endswith(ext) for ext in allowed_extensions)

    return domain_valid and extension_valid

def otp_verification_flow(email, name):
    otp = generate_otp()
    if not send_email(email, otp, name):
        return

    user_otp = input("Enter the OTP received in your email: ")

    if user_otp.isdigit() and int(user_otp) == otp:
        print("✅ OTP verified successfully!")
    else:
        print("❌ Invalid OTP!")
        retry = input("Do you want to resend OTP on same email? (yes/no): ").strip().lower()
        if retry == "yes":
            otp_verification_flow(email, name)
        elif retry == "no":
            new_email = input("Enter new email: ").strip()
            while not email_verification(new_email):
                print("❗ Invalid email format.")
                new_email = input("Enter a valid email: ").strip()
            otp_verification_flow(new_email, name)
        else:
            print("❗ Invalid input. Exiting.")

# Main flow
print("🔐 Secure Email OTP Verification\n")
name = input("Enter your name: ").strip()
email = input("Enter your email ID: ").strip()

while not email_verification(email):
    print("❗ Invalid email format. Try again.")
    email = input("Enter a valid email: ").strip()

otp_verification_flow(email, name)
