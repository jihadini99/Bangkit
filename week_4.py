#!/usr/bin/env python3
import os, sys
from PIL import Image

path = "supplier-data/images/"
files = os.listdir(path)

for file in files:
    if 'tiff' in file:
        name = os.path.splitext(file)[0]
        result = "supplier-data/images/" + name + ".jpeg"

        try:
            Image.open(path+file).convert("RGB").resize((600,400)).save(result, "jpeg")
        except IOError:
            print("cannot convert", file)

#!/usr/bin/env python3
import os, sys
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"

images = os.listdir(path)

for image in images:
  if image.endswith(".jpeg"):
    with open(path + image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})


#!/usr/bin/env python3
import os, sys
import json
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

files = os.listdir(path)

for file in files:
  if file.endswith("txt"):
    with open(path + file, 'r') as f:
      fruit_name = os.path.splitext(file)[0]
      data = f.read()
      data = data.split("\n")
      dictionary = {"name": data[0], "weight": int(data[1].strip(" lbs")), "descr$
      response = requests.post(url, json=dictionary)
      response.raise_for_status()

      print(response.request.url)
      print(response.status_code)


#!/usr/bin/env python3

import reports
import emails
import os, datetime

date = datetime.datetime.now().strftime('%Y-%m-%d')

def pdf_generate(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if file.endswith(".txt"):
      with open(path + file, 'r') as f:
        line = f.readlines()
        weight = line[1].strip()
        name = line[0].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf


if __name__ == "__main__":
  path = "supplier-data/descriptions/"
  files = "Process Updated on " + current_date 
  #generate the package for pdf body
  pdf_file = generate_pdf(path)
  reports.generate_report("/tmp/processed.pdf", title, pdf_file)

  #generate email information
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  
  #generate email for the online fruit store report and pdf attachment
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)


  #!/usr/bin/env python3

import reports
import email
import os, datetime

date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if file.endswith(".txt"):
      with open(path + file, 'r') as f:
        inline = f.readlines()
        weight = inline[1].strip()
        name = inline[0].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  path = "supplier-data/descriptions/"
  title = "Process Updated on " + date
  pdf_file = generate_pdf(path)
 # reports.pdf_generate(attachment, title, paragraph)
  reports.generate_report("/tmp/processed.pdf", title, pdf_file)
#content
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  paragraph = "All fruits are uploaded to our website successfully. A detailed li$
  attachment = "/tmp/processed.pdf"

  information_result = emails.generate_email(sender, receiver, subject, paragraph$
  emails.send_email(information_result)


#!/usr/bin/env python3

import email
import mimetypes
import os
import smtplib


def email_generate(sender, recipient, subject, body, attachment_path):
    result = email.message.EmailMessage()
    result["From"] = sender
    result["To"] = recipient
    result["Subject"] = subject
    result.set_content(body)


    if not attachment_path == "":
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)

    return result


def send_email(result):
    mail_server = smtplib.SMTP('34.133.175.76')
    mail_server.send_message(result)
    mail_server.quit()



#!/usr/bin/env python3
import reports
import emails
import os
from datetime import date

desc = os.path.expanduser('.') + '/supplier-data/descriptions/'
files = os.listdir(desc)

report =[]

def pdf_generate(data):
    for item in data:
        report.append("name: {}"<br/>weight: {}\n".format(item[0], item[1]))
    return report

text = []
for file in files:
    with open(desc + file, 'r') as f:
        text([line.strip() for line in f.readlines()])
        f.close()

if __name__=="__main__":
    summary = pdf_generate(text)
    paragraph = "<br/><br/>".join(summary)
    title = "Processed Update on {}\n".format(date.today().strftime("%b %d, %Y"))
    attachment = '/tmp/processed.pdf'

    reports.generate_report(attachment, title, paragraph)

    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email.""

    result = emails.generate_email(sender, recevier, subject, body, attachment)
    emails.send_email(result)
