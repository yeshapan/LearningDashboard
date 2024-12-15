### Learning Path Dashboard
A web application that allows instructors to create mini-courses with various content types (PDF, text, images, links, videos), track student progress, and facilitate community engagement. Built with Django, MySQL, and Vue.js.

Goal of the project is to make a learning path dashboard web app

### 📑Features

## Features

- **Two primary users**: Instructor and Student

### Instructor Features
- Instructors can design micro-courses by uploading content in the form of:
  - Text
  - PDFs
  - Links to external videos, etc.
- Instructors must get their profile verified by the organization they work for before publishing a course. This helps maintain the integrity of the platform.
  
### Student Features
- Students can enroll in courses.
- Students can view live progress for a course, allowing both students and instructors to track progress in real-time.
  - This helps provide timely feedback and correction from the instructor if needed.

### Community Features
- A **Community page** is available to facilitate peer engagement and support.
  
### Marketplace Features
- A **Marketplace** recommends similar courses to students, helping them explore more relevant content.

## Use Cases

- **Educational Institutions**: This platform can be used as part of the evaluation criteria within educational institutions, enabling instructors to design and manage micro-courses, and allowing students to enroll and track their progress.
  
- **Non-Profit Organizations**: The platform can also be used by volunteers and non-profit organizations to provide e-education to underprivileged children at a low cost, especially since many platforms like Coursera, Udemy, etc., are paid and expensive.



## Installation Instructions

Follow the steps below to set up the project locally and push your changes to GitHub.

### Prerequisites

- Python 3.x
- MySQL
- Node.js and npm (for the Vue.js frontend)
- Git

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/learning-path-dashboard.git
cd learning-path-dashboard
```

### Step 2: Set Up Virtual Environment

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - **Windows (PowerShell)**:
      ```bash
      .\venv\Scripts\Activate
      ```

3. Install the required dependencies:

    ```bash
    pip install django mysqlclient
    ```

### Step 3: Set Up MySQL

1. Create a MySQL database for the project:

    ```bash
    CREATE DATABASE learning_dashboard;
    ```

2. Configure the database settings in your `settings.py` file. Update the `DATABASES` section with your MySQL credentials.

### Step 4: Apply Migrations

Run the following command to apply the initial migrations:

```bash
python manage.py migrate
```
### Step 5: Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```
### Step 6: Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```
### Step 7: Vue.js Setup (Frontend)

To set up the frontend (Vue.js):

1. Navigate to the `frontend` folder (create a separate folder for Vue.js if needed).
2. Install Vue.js dependencies:

    ```bash
    npm install
    ```

3. Run the Vue.js development server:

    ```bash
    npm run serve
    ```

### Step 8: Pushing Changes to GitHub

1. **Add changes to the staging area**:

    ```bash
    git add .
    ```

2. **Commit your changes**:

    ```bash
    git commit -m "Initial commit"
    ```

3. **Push to your remote repository**:

    ```bash
    git push -u origin main
    ```



