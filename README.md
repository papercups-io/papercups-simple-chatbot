### to activate environment
`python3 -m venv env`
`source env/bin/activate`
`pip install -r requirements.txt`


### Download model, untar, and move in to models folder
 `wget https://tfhub.dev/google/universal-sentence-encoder/4?tf-hub-format=compressed`

### save new libraries 
`python -m pip install Flask==1.1.1` < example
`python -m pip freeze > requirements.txt`


### Start app
export FLASK_ENV=development; python app.py

