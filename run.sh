# export FLASK_DEBUG=1
# export FLASK_APP=temp.py flask run

FLASK_APP=server.py FLASK_DEBUG=1 python -m flask run --host=0.0.0.0 --port 5000
