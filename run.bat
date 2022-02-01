python -m pip install -U pip setuptools virtualenv --user 
python -m virtualenv .venv 
.venv\scripts\activate
python -m pip install -r requirements.txt

cd src 
python get_facts.py --config C:\Users\Vamshi\Documents\interview\catfacts\config\config.yaml