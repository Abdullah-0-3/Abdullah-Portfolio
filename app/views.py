from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import ContactMessage
from . import db, mail
from flask_mail import Message

views = Blueprint('main', __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/services')
def services():
    return render_template("services.html")

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Save message to the database
        new_message = ContactMessage(name=name, number=number, email=email, subject=subject, message=message)
        db.session.add(new_message)
        db.session.commit()

        # Send email to the site owner
        owner_msg = Message(subject=f"New Contact from {name}",
                            sender=email,
                            recipients=['abdullahabrar4843@gmail.com'])
        owner_msg.body = f"Name: {name}\nNumber: {number}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(owner_msg)

        # Send confirmation email to the user
        user_msg = Message(subject="Thank you for contacting us!",
                           sender='abdullahabrar4843@gmail.com',
                           recipients=[email])
        user_msg.body = f"Hello {name},\n\nThank you for contacting me! I appreciate you taking the time to reach out. I’ve received your message and will get back to you as soon as possible.\nIn the meantime, if you need any further assistance, feel free to let me know.\n\nRegards,\nMuhammad Abdullah Abrar"
        mail.send(user_msg)

        flash('Message Sent!', 'success')
        return '', 200  # Returning 200 for JavaScript success handling

    return render_template("contact.html")