# Phase 3 CLI Project 

This project is a basic workout tracker. It showcases a one-to-many relationship.
The user inputs their name. Then they enter the workout information. The information is then added to the tables.

To use this tracker you need to fork and clone the repo. Open it on your local machine and run pipenv install pipenv shell. You also need to run pip install sqlalchemy faker click 
Upon entering the shell and running either add_user.py or delete_user.py, you will be met with a prompt. Answer the quesitons by typing directly in the command line. 
The inputs will be added to the correct tables.

To interact with the tables run python add_user.py add-user to add a user and delete_user.py delete-user to delete a user, then simply input a date for the workout, and for the user input name, age and sport for the user.