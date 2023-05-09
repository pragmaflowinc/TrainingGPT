###venv
source venv/bin/activate

###Prepare document
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>


###Install correct venv:
sudo apt-get update -y 
sudo apt-get install python3.10-venv

###Install Requirements
pipenv requirements > requirements.txt
pip install -r requirements.txt