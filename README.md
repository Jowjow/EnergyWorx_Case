# EnergyWorx_Case
A Development Case for EnergyWorx

# Virtual Environment: 

For creating and activating a standard python virtual environment do:

```python3 -m venv ewx_env -> source /ewx_env/bin/activate```

A custom env(Anaconda etc) or existing venv can be used.

For setting up all the necessary dependencies one should run:

```pip install -r requirements.txt ```

# Database 
A database file already populated with some entries is also present in this repository, it was created using sqlite3. If another SQL database is to be used the single table creation query is:

```sql
CREATE TABLE Url_Shorten (
    Url varchar(255),
    ShortCode varchar(7),
    CreatedAt timestamp,
    LastRedirect timestamp,
    RedirectCount int 
); 
```


# Running the Server

Once into your (or the provided) Python Virtual environment to start the server run: 

```python server.py```


# Unit Tests 

To run the unit tests run:

```python -m unittest unit_tests.py```
