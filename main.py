import yagmail
from dotenv import load_dotenv
import os
from tkinter import *
from tkinter.filedialog import askopenfilename

load_dotenv() # load .env variables

# get environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# upload attachment
def uploadAttachment(event=None):
    global attachment_name 
    global attachment
    attachment = askopenfilename()
    attachment_name.set(os.path.basename(attachment))

# send email
def sendEmail(to = email, subject = None, body = None, attachment = None): 
    # set up email server
    try:
        yagmail.register(email, password)
        yag = yagmail.SMTP(email)
        yag.send(to = to, subject = subject, contents = [body, attachment])
        return "success"
    except Exception as e:
        return e
    

if __name__ == "__main__":
    # initialize gui
    root = Tk() 
    root.title("Email Sending Interface")
    root.configure(background = "#f49242")

    # set up GUI

    # create header 
    top = Frame(root, bg = "#f49242")
    header = Label(top, text= "Send Your Emails Here!", bg = "#f49242", font = ("Sans Serif", 20), justify= CENTER)
    header.pack()
    top.pack()

    # create main fields
    body = Frame(root, bg = "#f49242")

    # recipients of email
    recipient_container = Frame(body,  bg = "#f49242")
    recipient_label = Label(recipient_container, text= "Recipient", font = ("Sans Serif", 16), bg = "#f49242", justify = LEFT)
    recipient_input  = Entry(recipient_container, font = "Helvetica", justify = LEFT)

    recipient_label.pack(padx = 10, pady = 20, side  = LEFT)
    recipient_input.pack(padx = 10, pady = 20, side = LEFT)
    recipient_container.pack()

    # subject of email if any
    subject_container = Frame(body,  bg = "#f49242")
    subject_label = Label(subject_container, text= "Subject", font = ("Sans Serif", 16), bg = "#f49242")
    subject_input  = Entry(subject_container, font = "Helvetica")

    subject_label.pack(padx = 15, pady = 15, side = LEFT)
    subject_input.pack(padx = 10, pady = 15, side = LEFT)
    subject_container.pack()

    # body of email
    body_container = Frame(body,  bg = "#f49242")
    body_label = Label(body_container, text= "Body", font = ("Sans Serif", 16), bg = "#f49242")
    body_input = Entry(body_container, font = "Helvetica", width = "20")

    body_label.pack(padx = 22, pady = 20, side = LEFT)
    body_input.pack(padx = 10, ipady = 20, pady = 35, side = LEFT)
    body_container.pack()

    # email attachments
    attachment_name = StringVar()
    attachment = ''
    attachment_container = Frame(body,  bg = "#f49242")
    attachment_button = Button(attachment_container, text = "Add Attachment", command = lambda *args : uploadAttachment()) 
    attachment_button.pack(padx = 25, side = LEFT)   
    attachment_label = Label(attachment_container, textvariable = attachment_name)
    attachment_label.pack(padx = 10, side = LEFT )    
    attachment_container.pack(side = LEFT)
    

    # error messsage
    error_container = Frame(body,  bg = "#f49242")

    # buttons, (reset and submit)
    buttons_container = Frame(body,  bg = "#f49242")
    submit_button = Button(buttons_container, text = "Submit", command = lambda *args : sendEmail(recipient_input.get(), subject_input.get(), body_input.get(), attachment))
    submit_button.pack()
    buttons_container.pack()

    # pack everything all together
    body.pack()

    # run gui
    root.mainloop()

    

