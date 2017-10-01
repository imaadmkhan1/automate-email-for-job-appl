import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
company_dict = {'google': 'careers@google.com', 'Facebook': 'careers@facebook.com', 'Microsoft': 'careers@microsoft.com'}
for key, value in company_dict.iteritems():
    fromaddr = "imaad@gmail.com"
    toaddr = value

    msg = MIMEMultipart()

    msg['From'] = "Imaad Mohamed Khan"
    msg['To'] = toaddr
    msg['Subject'] = "Application at"+" "+key


    body = "Hi"+" "+key+" "+"team,\nTrust this mail finds you in the pink of your health. Who writes opening lines like these?\nBest Regards,\nImaad Mohamed Khan"

    msg.attach(MIMEText(body, 'plain'))

    filename = "Imaad_CV.pdf"
    attachment = open("Imaad_CV.pdf", "r+")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Enter Password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
