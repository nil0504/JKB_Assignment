## This is a simple web application that allows users to input data, validate it, store it in a database, retrieve it, and display it in a tabular format.

## Prerequisites
Before you begin, ensure you have met the following requirements:
1.Python (3.x)
2.Django (3.x)
3.SQLite database (default in Django)
4.Clone the Git repository to your local machine
5.Setup Database(python manage.py migrate)
6.Start Developement Server(python manage.py runserver)


## Use:
1.Open your web browser and visit http://localhost:8000 to access the user registration form.
2.Fill out the form with valid data and submit it.
3.if your email is already saved in the database then it will directly show you the details that are already saved with that email.
4.if your age is 0 or age and calculated age from your date of birth are not same then it will redirect you to the same page with an error message.
5.if you enter valid details then it will save your data in database and redirect you to the Your_details page where you can see all the data in table format
6.you can also view data by visiting http://localhost:8000/Your_details.
