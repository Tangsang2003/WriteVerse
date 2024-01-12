# WriteVerse
#### Video Demo: https://youtu.be/eZeO4jWgudI
#### Description:
## WriteVerse: Express and Share 📖
WriteVerse is a simple web application project that allows users to express their 
thoughts and ideas through blogs and share them. 📝🌐 This project
was conceived as part of fulfilling requirements for CS50's final project.
I extend special thanks to Corey Schafer for his invaluable Flask
tutorials. WriteVerse is a project, a functional web-application through 
which I have refined my skills in Flask and database management.
🚀🔧 HTML, CSS, and Bootstrap contribute to the simplistic front-end,
and Flask drives the robust back-end, and Jinja2 dynamically generates
web pages. Python packages, listed in requirements.txt file form the
backbone of functionality.
## Features📢
<ul>
<li>User Authentication 🔐</li>
- Securely manages user identities and access.
<li>Login Page🚪</li>
- A seamless entry point for users.
<li>Users can create and blog/content posts ✍️</li>
- Users can effortlessly craft and refine their posts.
<li>Profile customization 🖼️</li>
- Users can personalize their profile with their own profile pictures.
<li>Explore other's posts 👀</li>
- Users can not only publish their own posts but also explore posts by other fellow users.
<li>Edit and delete their posts 🗑️</li>
- Flexibility to edit and delete already published posts.
<li>Custom Error Handler pages ⚠️</li>
- UserFriendly Error Handling pages.
<li>Password Recovery🔐</li>
- Users can reset their password if they have forgotten it. A functionality
to send reset link to the registered email has been implemented.
</ul>
<br>
<h2>Setup</h2>
<ul>
    <li>Clone the repository. 🧬</li>
git clone https://github.com/Tangsang2003/WriteVerse.git
    <li>Set up a virtual environment. 🌐</li>
    <li>Install all the packages listed in the requirements.txt file. 📦</li>
pip install -r requirements.txt
    <li>Set up the environment variables listed below. You need to set them up appropriately:
        <ul>
            <li>'SECRET_KEY' // This variable is your secret key for secret operations.</li>
            <li>SQLALCHEMY_DATABASE_URI // This variable is the URI for your database. </li>
            <li>EMAIL_USER  // This is your email that you can set up to send reset links to other users.</li>
            <li>EMAIL_PASS  // This is the password to your email.</li>
        </ul>
    </li>
    <li>Finally, open the project directory in your terminal and execute 'python run.py'. 🚀</li>
    <li>Then, go to any of your browsers and visit: "localhost:5000". 🌐</li>
    <li>Then, explore the project. 🔍</li>
</ul>

## Project Structure
### Blueprints:

The project utilizes Flask Blueprints to organize the application into modular components.
Different functionalities such as user authentication, blog posts, and error handling are separated into individual blueprints.
This modular structure enhances maintainability and readability.
### Packages:
The project is organized as a package to encapsulate related modules.
The main application (__init__.py) serves as the entry point.
Subpackages (e.g., auth, main) contain specific functionalities.
### Database Models:
SQLAlchemy is employed as the ORM (Object-Relational Mapping) for database operations.
User and Post models are defined to structure the database schema.
Relationships between models (e.g., a user having multiple posts) are established.
### User Authentication:
Flask-Login is integrated for user authentication.
Login and logout functionalities are implemented.
User sessions are managed securely.
### Blueprint for Blog Posts:
A dedicated blueprint is created to handle blog-related functionalities.
Routes for creating, editing, and deleting posts are defined.
Post data is stored in the database, and users can perform CRUD operations on their posts.
### Profile Customization:
Users can customize their profiles by updating profile pictures and details.
The profile data is associated with the user model and stored in the database.
### Explore Others' Posts:
A feature to explore posts created by other users is implemented.
Users can view a feed of posts created by the community.
### Error Handling:
Custom error handler pages are created for a user-friendly experience.
Different HTTP error codes are handled with informative error pages.
### Password Recovery:
A password recovery feature is implemented.
Users can reset their password by receiving a reset link via email.
Flask-Mail is used for sending emails.
### Environment Variables:
Sensitive information such as the secret key, database URI, email user, and email password are managed as environment variables.
This ensures security by keeping confidential data out of the codebase.


<h1>Thank You ❤️ </h1>
Thank you for visiting this project. This project is a labor of love, 
and I invite you to contribute, edit, share, and customize the project
as you like. 

