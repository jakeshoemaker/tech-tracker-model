# :zap: Tech Tracker :zap: 

## Machine Learning Server Installation:

### 1. Install Python 3.8 or newer,can be downloaded at https://www.python.org/downloads/release/python-383/ as well as having Git installed
### 2. Clone repository
```
git clone https://github.com/jakeshoemaker/tech-tracker-model.git
```
### 3. install files from `requirements.txt`:
``` 
$ cd /current_dir/tech-tracker-model/api/
$ pip install requirements.txt
```
### 4. Train your own local ML model to replicate: 
```
$ python training.py
```
### 5. Run main.py to start the API Server for predictions:
```
$ python main.py
```

## Client Installation

0. Make Sure Node.Js is Installed on your system 
- https://nodejs.org/en/

### 1. Clone Repository or skip to 2 ->
```
git clone https://github.com/jakeshoemaker/tech-tracker-server.git
```
### 2. Change directory into frontend project located in 'tt-frontend'
#### | the Frontend client is embedded in my REST-Server's code. 
```
$ cd /currentdir/tech-tracker-server/tt-frontend/
```
### 3. Initialize the node project by running 
```
$ npm install 
```
### OR if you use yarn as your package manager use:
```
$ yarn
```

### 4. You will need to create a .env file in the folder `/tt-frontend/` with the following Keys:

.env file:
```
REACT_APP_API_KEY = "insert API key here"
```
** note this key can be found from https://www.quandl.com/sign-up **
### 5. After saving the file run the following commands in your terminal:
```
npm run start
```

Have fun using tech-tracker :grin:
