# pysim
A basic simulation of a world that can change. 

### Setup (mostly reminders on using venv)

#####Create and activate a new virtual env:

`python3 -m venv pysim-env`

`source pysim-env/bin/activate`

(`deactivate` to get out)

On Macos installing this is slightly different, you can't install it via pip. So instead do:

`brew install python3-tk`

#####Install deps with requirements file:

`pip install -r requirements.txt`

(The installation for tkinter will fail if on macos but if you install it with the above instructions it'll be fine)

This will install: 

- tkinter
- some other stuff

### The World

### The Inhabitants

An interesting implementation for bad guy AI would be to retrain the AI based off player movements after some period of time so behavior is constantly changing. Can we do that with a 2d shapes game to start?

