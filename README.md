# DRF_test


1 hour test


Please only take one hour to fix the bugs and add to the backend found in the github repository 

The areas that need the most attention 

There are circular import issues for Profile and Company
The registration, although it creates the new user, there is an error on the drf interface
The database design found on https://dbdiagram.io/d/62a1981954ce2635278e1984 may not be accurate and needs to be fixed to allow any user to connect with any company and visa versa.  
The current model processes may not be the best way to structure the attributes

other steps

To create serializers, views and endpoints using the DRF framework
To add a create or put class to the company attribute found in the Profile model, so if a company already exists in the database, the user can edit the attributes instead of creating a new model.
To change the login to accept email and password instead of just username


Things to consider

Instead of using tools like postman please use the DRF framework, this is how I will be testing it.
You may have to remove certain models before you migrate so that the multiple user model works properly.
Providing a strong database design with strong drf practices is the point of the exercise.

