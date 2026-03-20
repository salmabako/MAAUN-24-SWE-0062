# Kubwa Business Hub

A local business directory web application built with Flask. Users can browse, add, edit, and delete business listings in the Kubwa community.

## What It Does

- View a directory of local businesses, shown in order of most recently added (Stack / LIFO)
- Add a new business with a name, category, and description
- Edit existing business details
- Delete a business (with a confirmation prompt)
- Each listing is automatically timestamped when created

## How It Works (Behind the Scenes)

- **Object-Oriented Programming**: The app uses a `Business` class to represent each listing and a `Directory` class to manage the collection. All logic is encapsulated in class methods.
- **Stack Data Structure**: Businesses are stored in a list used as a Stack. New entries are pushed with `.append()` and displayed in LIFO (Last-In, First-Out) order so the newest listings appear first.
- **datetime Module**: Each business gets a creation timestamp using Python's built-in `datetime.now()`, formatted into a readable string like "Mar 20, 2026 - 02:30 PM".

## How to Run It Locally

Follow these steps to get the app running on your computer:

### 1. Clone the repository

```bash
git clone https://github.com/salmabako/MAAUN-24-SWE-0062.git
cd MAAUN-24-SWE-0062
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On Mac/Linux:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

### 4. Install Flask

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
python app.py
```

### 6. Open in your browser

Go to: [http://localhost:8080](http://localhost:8080)

You should see the Kubwa Business Hub home page with a sample business already listed.

## Project Structure

```
MAAUN-24-SWE-0062/
├── app.py             # Flask routes and server setup
├── models.py          # Business and Directory classes (OOP + Stack)
├── requirements.txt   # Python dependencies
├── templates/
│   ├── index.html     # Home page - displays all businesses
│   ├── add.html       # Form to add a new business
│   └── edit.html      # Form to edit an existing business
└── README.md
```
