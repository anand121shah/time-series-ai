from flask import Blueprint, render_template, request, redirect, url_for, flash
import datetime

main = Blueprint('main', __name__)

# Provide current year for the footer
@main.app_context_processor
def inject_current_year():
    return {'current_year': datetime.datetime.now().year}

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Thank you for reaching out, {name}! We’ll get back to you soon.', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')

@main.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

