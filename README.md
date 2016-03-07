# # simple_gevent

This is a  python program script to initiate multiple requests within your local server , It has two components , one is the listner and another one fire requests on the listner

### USAGE
1. ```pip install requirements.txt```

1. Initiate the listner script by specifying the port number as argument to script

```python gevent-listner.py 9000 ```

2. Initiate the requests to the server by sepcifying the port number and the number of requests as argument to script, Below command would fire up 200 concurrent requests on port 9000 of your local server

```python gevent-fire.py 9000 200```
