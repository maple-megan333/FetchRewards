This is my assignment for the FetchRewards backend apprenticship take home test. 
The goal was to create an API that could add transactions. 

This project is created in a virtual enviornment that includes all the important python libraries. 
to activate your virtual enviornment in your terminal go to the newfetch\fetch
and activate the fetch virtual enviornment with any of the following methods. 
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

Once active make sure to install some important stuff by typing these in your command prompt:
pip install flask
pip install sqlalchemy
pip install flask_sqlalchemy
pip install datetime
pip install flask_wtf
pip install wtfforms

some of these are extra but good to have if we want to make our application work on the front end!


To work with this application go to:
https://web.postman.co/
login or sign in. 
download the desktip agent extention. 
go to 'My Workspaces' and create a new tab. 

In your terminal still in the fetch enviornment type in: flask run
copy the http:// address next to "running on" and input it into the bar ned to the drop down menu for the method type

Add transactions: add 'add_points' to the end of your base html address and toggle the method type to post. 
select body and raw and in the text area below enter your transaction filling in the paramerters:
    {
    "payee"= payee-name, 
    "points"= number of points, 
    "timestamp = (mm-dd-yyyy 00:00:00)
    }
    timestamp is an optional parameter as it is auto set to input time of entry. Currently only the three vendors listed on the assignment are included, please ensure you only use one of these payees
select send

spend points: add 'spend_points' to the end of your base html address and toggle the method type to post. 
select body and raw and in the text area below enter your transaction filling in the paramerters:
    {
    "points"= number of points, 
    }
select send

Get balances: add 'balences' to the end of your base html address and toggle the method to get.
select body and none as your sub parameters 
select send




    
