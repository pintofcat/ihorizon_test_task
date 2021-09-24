# how to test run
pip install -r requirements.txt 
./manage.py runserver


# database data
there are 3 users in database(`db.sqlite3`), exclude `admin`.
You can check all flow with them:
- login: `customer`, password: `customer`
- login: `customer1`, password: `customer`
- login: `agent`, password: `agent`
