# Tuition-Management-Software
- pip install django
- Install MS SQL
> Database name: TutionManagementSoftware
>> - Username: dbmsprojectlogin
>> - Password: dbms
>> - Run the sql file inside MS SQL
- python manage.py inspectdb > tuitionapplication/models.py
- Save the models.py as UTF-8 encoding
- For Email: 
> In settings.py
>> #Email settings
>> - EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
>> - EMAIL_HOST = 'smtp.gmail.com'
>> - EMAIL_PORT = 587
>> - EMAIL_USE_TLS = True
>> - EMAIL_HOST_USER = 'abc@vitstudent.ac.in' #put your vit email id here (make sure you have allowed less secure apps in settings in your gmail)
>> - EMAIL_HOST_PASSWORD = 'pass123' #put your password of gmail here
>> - (After using the app make sure to turn off less sure apps settings, orelse email might be compromised)
- python manage.py runserver
