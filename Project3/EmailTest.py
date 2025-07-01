import smtplib

try:
    server = smtplib.SMTP_SSL("smtp.qq.com", 587)

    server.login("1210604280@qq.com", "hdhvdspujinfhgbb")

    print("Login successful!")

except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Please check your email and password.")

except smtplib.SMTPException as e:
    print(f"SMTP Error occurred: {str(e)}")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

finally:
    if 'server' in locals():
        server.quit()