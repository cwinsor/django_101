
# confirm at least we have python with pip
python --version
python -m pip --version

# add virtualenv if user doesn't have it
python -m pip install virtualenv

# create an empty virtualenv
python -m virtualenv pymote_env --no-site-packages

# activate the (empty) virtualenv
.\pymote_env\Scripts\activate

# get the libraries specified in requirements.txt
pip install -r requirements.txt
