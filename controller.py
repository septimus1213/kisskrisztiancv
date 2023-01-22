from flask import render_template, url_for, request, redirect
from changemodel import *

def HomePage():
    if request.method == "POST":
        way = request.form.get("way")
        if way == "next":
            num = 1
        else:
            num = -1
        number = request.form.get("number")
        number = int(number) + num
        if number > 3:
            number = 0
        if number < 0:
            number = 3
    else:
        num = 0
        number = 0
    model = Change(number)
    
    return render_template("index.html", number=number, model=model)