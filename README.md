# Personal Blogging Application

##Project Description
This project is a simple blogging web application built using Flask, SQLite, HTML and CSS.
The application allows users to:

Create blog posts
Read blog posts
Update blog posts
Delete blog posts
Add comments to posts

The purpose of the project was to practice backend web development concepts such as Flask routing, CRUD operations, database integration, form handling and template rendering.

Technologies Used

Python
Flask
SQLite
HTML
CSS
Jinja Templates
Git and GitHub


Setup and Installation

Clone the Repository

git clone https://github.com/kalaisanthi29/PersonalBloggingApplication.git

Open the Project Folder

cd PersonalBloggingApplication

Install Flask

pip install flask

Run the Application

python app.py

Running the Application Locally
After running the application, open the following link in a browser:
http://127.0.0.1:5000

Project Structure
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

Security
The application uses parameterised SQL queries with ? placeholders to help prevent SQL injection attacks.
Example:
conn.execute(
    "INSERT INTO posts (title, body) VALUES (?, ?)",
    (title, body)
)

AI Assisted Tools
AI assisted tools were used during development for debugging Flask and Git issues, understanding Flask routing and CRUD operations, troubleshooting template and database errors and learning best practices for SQL security and project structure. I used these tools to help understand concepts and fix errors, but tested and adjusted everything myself.

Known Limitations

No user authentication system
No password protection
Minimal frontend styling
Comments cannot currently be edited or deleted
No search functionality


Future Improvements
If given more time, the following could be added:

User login and registration
Improved responsive design and styling
Search and category filtering
Flash messages for user feedback
Ability to edit and delete comments
Better error handling and validation
