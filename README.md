# Fetch Backend Internship Challenge

## How to install and run the project
1) Since this is a Python application, you will need python3. If you do not have python3 installed, make sure you download it from [here](https://www.python.org/downloads/) and select the "Add Python to PATH" checkbox during the installation.
2) Clone this repo to your local machine by doing the following in your terminal:
   
   i) `git clone https://github.com/SajithDev/fetch-backend-internship-challenge.git`<br />
   ii) `cd fetch-backend-internship-challenge`
   
4) A virtual environment can be used so that the required dependencies do not interfere with your local machine's current packages. In your terminal enter the following:
   
   i) `python3 -m venv venv` <br />
   ii) Windows: `.\venv\Scripts\activate` or Mac: `source venv/bin/activate` <br />
   
5) Install the dependencies
   `pip install -r requirements.txt`
   
6) Run flask application on port 8000 by entering `flask run --port=8000` <br />
   You should see the following output: <br />
  ```
 * Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
  ```
6) Go to `http://127.0.0.1:8000` in your browser to access the running server.

## Interacting with API endpoints
There are 3 endpoints in this application: 

i) Add points (POST) route: `/add` <br /> ii) Spend Points (POST), route: `/spend` <br /> iii) Get Points Balance (GET), route: `/balance`

### You can send and receive JSON requests by downloading the [Postman Agent](https://www.postman.com/downloads/postman-agent/) and using the [Postman web application](https://www.postman.com/).
Select `Body` and `raw` as seen in the image and send your JSON body.
![image](https://github.com/user-attachments/assets/56eb4ebc-ee88-41ff-9d8e-4ba053fcb77e)
