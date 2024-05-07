
### Install packages

install requirements using pip 

```
$ pip install -r requirements.txt
```

### Run the backend using uvicorn

I've added the "uvicorn" package as a requirement to run the FastAPI server. Run the server like this:

```
$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

If everything worked, you should see something like this in the console and the server will start up on http://0.0.0.0:8000

```
INFO:     Will watch for changes in these directories: ['/Users/asimmittal/Desktop/coh-th-ex/product-engineer-starter/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [78350] using StatReload
INFO:     Started server process [78352]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```