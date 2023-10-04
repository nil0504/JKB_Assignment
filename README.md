## This simple web application allows users to input data, validate it, store it in a database, retrieve it, and display it in a tabular format.

## Prerequisites
Before you begin, ensure you have met the following requirements:
1. Python 
2. Django 
3.SQLite database (default in Django)
4. Clone the Git repository to your local machine
5.Setup Database(python manage.py migrate)
6.Start Developement Server(python manage.py runserver)


## Use:
1. Open your web browser and visit http://localhost:8000 to access the user registration form.
2. Fill out the form with valid data and Submit it.
3. if your email is already saved in the database, it will directly show you the details already saved with that email.
4. if your age is 0 or your age and calculated age from your date of birth differ, it will redirect you to the same page with an error message.
5. if you enter valid details, then it will save your data in the database and redirect you to the Your_details page, where you can see all the data in table format
6. you can also view data by visiting http://localhost:8000/Your_details.


## Database Schema
class user_registration(models.Model):
    Id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=40)
    Email = models.CharField(max_length=50)
    Age=models.IntegerField()
    Date_of_Birth=models.DateField()
