from flask import Flask, render_template, request, redirect, session
import ibm_db
import re
app = Flask(__name__)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/about')
def about():
    
    return render_template('about.html')
@app.route('/privacyterms')
def privacyterms():
    return render_template('privacyterms.html')