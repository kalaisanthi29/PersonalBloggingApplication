# Personal Blogging Application

## Project Description

This project is a simple blogging web application built using Flask, SQLite, HTML, and CSS.

The application allows users to:
- Create blog posts
- Read blog posts
- Update blog posts
- Delete blog posts
- Add comments to posts

The purpose of the project was to practice backend web development concepts such as Flask routing, CRUD operations, database integration, form handling, and template rendering.



## Features

- Create new blog posts
- View all blog posts
- View individual blog posts
- Edit existing blog posts
- Delete blog posts
- Add comments to blog posts
- SQLite database integration
- SQL injection protection using parameterized queries



## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja Templates
- Git & GitHub



## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kalaisanthi29/PersonalBloggingApplication.git
```

### 2. Open the Project Folder

```bash
cd PersonalBloggingApplication
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```



## Running the Application Locally

After running the application, open the following link in a browser:

```text
http://127.0.0.1:5000
```



## Project Structure

```text
PersonalBloggingApplication/
│
├── app.py
├── database.py
├── blog.db
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── create_post.html
│   ├── edit_post.html
│   └── post.html
```

---

## Security Measures Implemented

The application uses parameterized SQL queries with `?` placeholders to help prevent SQL injection attacks.

Example:

```python
conn.execute(
    "INSERT INTO posts (title, body) VALUES (?, ?)",
    (title, body)
)
```

This ensures that user input is safely handled before interacting with the database.



## AI-Assisted Tools

AI-assisted tools were used during development for:
- Debugging Flask and Git issues
- Understanding Flask routing and CRUD operations
- Troubleshooting template and database errors
- Learning best practices for SQL security and project structure

All code was reviewed, tested, and modified during development.



## Known Limitations

- No user authentication system
- No password protection
- Minimal frontend styling
- Comments cannot currently be edited or deleted
- No search functionality



## Future Improvements

If given more time, the following improvements could be added:
- User login and registration
- Improved responsive design and styling
- Search and category filtering
- Flash messages for user feedback
- Ability to edit and delete comments
- Better error handling and validation
