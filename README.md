# carp.web
web of carp

# How to install
```bash
$ pip install -r requirements.txt
$ cp .env.sample .env
$ vi .env

FLASK_ENV=produciton

CARP_DATABASE_URI=mysql+pymysql://${USER}:${PASS}@${ENDPOINT}/${DATABASE}
```

# RUN
```bash
$ python3 application.py
```