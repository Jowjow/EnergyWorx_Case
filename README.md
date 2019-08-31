# EnergyWorx_Case
A Development Case for EnergyWorx

# Virtual Environment:
The whole virtual environment with all needed libs for running this piece of code is present in this repository. 

For accessing it clone the repo and do:

cd /$REPO_HOME -> source ewx_env/bin/activate

If the reader wants to create a custom env(Anaconda or others) from scratch he can, for setting up all the dependencies he shuld run:

pip install -r requirements.txt  

# Database 
A database file already populated with some entries is also present in this repository, it was created using sqlite3. If another SQL database is to be used the single table creation query is:

""" CREATE TABLE Url_Shorten (
    Url varchar(255),
    ShortCode varchar(7),
    CreatedAt timestamp,
    LastRedirect timestamp,
    RedirectCount int 
); """


# Running the Server

Once into your (or the provided) Python Virtual environment to start the server run: 

python server.py


# Unit Tests 

To run the unit tests run:

python -m unittest unit_tests.py
