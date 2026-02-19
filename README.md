# Amalitech Sure Cure Vault Test

A Next.js-based web application for managing secure vault functionality.
This project includes a backend built with Django and is configured for deployment on **Vercel**.

---

## 🚀 Project Overview

This is a web application built with:

* Python (Django framework)
* SQLite database
* Static frontend assets Next.js (CSS/JS) 
* Deployment configuration for **Vercel**

---

## 📦 Prerequisites

Before running this project locally, make sure you have:

* Python 3.8 or higher
* pip (Python package manager)
* Git
* Virtual environment tool (`venv` recommended)

You can download Git from **GitHub** if not installed.

---

## 🔽 How to Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/lilcoded7/amalithech-sure-cure-vault-test.git
```

Then navigate into the project folder:

```bash
cd amalithech-sure-cure-vault-test
```

---

## 🛠️ How to Set Up and Run the Project Locally

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate the Virtual Environment

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Create a Superuser (Optional but Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

---

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

You should see something like:

```
Starting development server at http://127.0.0.1:8000/
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure Overview

```
amalithech-sure-cure-vault-test/
│
├── accounts/          # User authentication app
├── vault/             # Core vault functionality
├── staticfiles/       # Static assets
├── manage.py          # Django project manager
├── db.sqlite3         # SQLite database
├── requirements.txt   # Project dependencies
├── vercel.json        # Vercel deployment config
```

---

## 🌍 Deployment

This project includes a `vercel.json` configuration file, meaning it is ready for deployment on **Vercel**.

To deploy:

1. Push your changes to GitHub.
2. Import the repository into Vercel.
3. Configure environment variables if required.
4. Deploy.

---

## ⚠️ Important Notes

* Do not commit sensitive environment variables.
* For production use, configure proper database and security settings.
* SQLite is suitable for development but not recommended for production.

---

## 👨‍💻 Author

Developed by lilcoded7.

---

If you'd like, I can also create a more **professional README for job/portfolio submission**, including badges and screenshots.
