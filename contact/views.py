from pprint import pprint
from django.shortcuts import render
from acount.models import CustomerProfile

# Create your views here.
import smtplib

from contact.models import Contact
from listings.models import Listing


def send_email(subject, message, receiver_address="yawapen977@acentni.com"):
    # Your email address and password
    sender_address = "meriemmeriem19alg@gmail.com"
    sender_password = "hblx yslt dqze pnju"

    # Set up the subject and body of the email
    header = f"\r\nSubject: {subject}"
    body = f"\r\n{message}"

    # Combine the headers and the body
    combined = header + body

    # Send the email!
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_address, sender_password)
    server.sendmail(sender_address, receiver_address, combined)
    print("Email sent!")
def contact(request):
    if request.method == "POST":
      listing=request.POST.get('listing','')
      username=request.POST.get('name','')          
      phone=request.POST.get('phone','')          
      email=request.POST.get('email','')          
      message=request.POST.get('message','') 
      sujet='contact sur '+listing 
      send_email(sujet,message,email)
      pprint(request.POST)
      listing=Listing.objects.get(id=listing)
      contact=Contact(
            listing=listing,
            customer=request.user.customerprofile,
            email=email,
            subject=sujet,
            content=message
      )
      contact.save()
#context pour envoyer en template
    return render(request, 'pages/dashboard.html')
