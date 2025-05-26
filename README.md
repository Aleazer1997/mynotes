
## Cloning and starting application
1. - git clone https://github.com/aleazer1997/mynotes

# For the frontend
1. - cd frontend
2. - npm install
3. - npm start  //STARTS REACT SERVER

# For the backend
## ✅ Prerequisites
Ensure the following are installed:
- Python (3.8+)
- Git
- pip (Python package installer)
- Virtual environment tool (`venv` or `virtualenv`)
- (Optional) PostgreSQL or other database if used

---

## 1. Create a Virtual Environment
```bash
python -m venv venv
# For Linux/macOS:
# python3 -m venv venv
```

---

## 2. Activate the Virtual Environment

### On Windows:
```bash
venv\Scripts\activate
```

### On macOS/Linux:
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables
- Create a `.env` file if required (look for `.env.example`)
- Or update `settings.py` with necessary values:
  - `SECRET_KEY`
  - `DEBUG`
  - `DATABASES`

---

## 5. Apply Migrations
```bash
python manage.py migrate
```

---

## 6. Create a Superuser (Admin Panel Access)
```bash
python manage.py createsuperuser
```

---

## 7. Run the Development Server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)


# Notes List
<img src="Notes.PNG">  
