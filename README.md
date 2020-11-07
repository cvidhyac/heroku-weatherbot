# heroku-weatherbot

Initial demo project to try using free heroku plan

## What does the webhook do?
- Simple Flask POST api call to openweathermap.org to fetch forecast for the next five days
- Try to integrate this with my personal slack account to see if it works

## Heroku notes
- Create a free account in heroku
- Explore the console
- Understand different Linux Dynos
- 400 free hours per month (Really nice!!)

## Heroku CLI

Install :

```
brew tap heroku/brew && brew install heroku
```

Good to know commands :

```
heroku login -i
Email: myemail@whatever.com
Password: changeit

heroku access --app cvidhyac-weatherbot

```

To scale down and save dynos:
```
heroku ps:scale web=0 --app cvidhyac-weatherbot

```

Example output:

```
Scaling dynos... done, now running web at 0:Free
```

