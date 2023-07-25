# Student Hub

Student Hub is simple CRUD based project where user can make their own To-Do list, take notes with markdown and also Pomodoro,you can search your notes. Not only that, they can SignUp using form or they can register through Github, Google.I have also added feature of Changing password and forgot you password.

## Home Page 

![App Screenshoot](https://media.discordapp.net/attachments/860002669141426176/1131005698990428280/image.png?width=1440&height=358)

## CREATING OF TO-Do LIST

![App Screenshoot](https://media.discordapp.net/attachments/860002669141426176/1131005877428699327/image.png?width=1440&height=608)

## CREATING AND MARKDOWN OF NOTES

![App Screenshoot](https://cdn.discordapp.com/attachments/860002669141426176/1131006383941234778/image.png)
![App Screenshoot](https://media.discordapp.net/attachments/860002669141426176/1131006507081793708/image.png?width=1440&height=408)

## LOGIN AND REGISTER THROUGH SOCIAL MEDIA 

![App Screenshot](https://media.discordapp.net/attachments/860002669141426176/1131006666297573386/image.png?width=1440&height=525)
![App Screenshot](https://media.discordapp.net/attachments/860002669141426176/1131006772547686470/image.png?width=1440&height=578)


## Installation

```bash
python -m venv .venv

python -m pip install -r requirement.txt

```
**Note**
you need to make .env file and populate ***SECRET KEY***.For that, you can create your own secret key by command `python -c "import secrets; print(secrets.token_urlsafe())"` and enter the value in .env file.If you feel uncomfortable for that then just, uncomment Security key in line 29 of settings.py file(Although it is not good practice)

Run **migration** and **collectstatic**

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic 
```

and finally run 
```bash
python manage.py runserver 
```
and go to **localhost:8000** or **127.0.0.1** for project to run

## Things I learned 

- Implementing of CRUD 
- Learn to Setup Social Media Login Provider like Google, Github as Login
- Learning to use different package of django like paperdown, allauth, whitenoise
- Learn proper deployement list for django (hosting part remaining)

## Reamining 

- [ ] To write test.py for both To-do and Note
- [ ] Prompt to ask user, that pomodoro will restart if they change the page.

**P.S** I am not that much confident in frontend, So pomodoro may not work fully for now and most of its code is taken as reference from other work. I will now learn abit more about frontend (CSS, JS) and make pomodoro abit more functionable. 


~~ MEOW



