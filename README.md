# Setup

```bash
# create virtual environment
python3 -m venv venv
# run virtual environment
source venv/bin/activate
# install python dependencies
pip install -r requirements.txt
```

# Dev

```bash
# watch scss changes
scss --watch scss:css

# run website generation
python3 app.py
# TODO : use watcher for changes in templates or in pages

# run local server
cd pages/
python3 -m http.server
```

# Deploy
