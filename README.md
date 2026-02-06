# Django ToDo App

A modern, feature-rich ToDo application built with Django 6.0 that helps you organize and manage your daily tasks efficiently.

## 📋 Features

- ✅ **Add Tasks**: Quickly add new tasks to your todo list
- ✏️ **Edit Tasks**: Update existing tasks with ease
- ✔️ **Mark as Done/Undone**: Toggle task completion status
- 🗑️ **Delete Tasks**: Remove unwanted tasks
- 📅 **Date Tracking**: Automatically track task creation and modification dates
- 📊 **Task Organization**: Separate views for pending and completed tasks
- 🎨 **Responsive Design**: Beautiful UI with Bootstrap 5
- 🔄 **Real-time Updates**: Instant task status changes

## 🛠️ Technologies Used

- **Backend**: Django 6.0.2
- **Database**: SQLite3
- **Frontend**: 
  - HTML5
  - Bootstrap 5.3.0
  - Font Awesome 4.7.0
- **Python Version**: 3.12
- **Dependencies**: 
  - asgiref 3.11.1
  - sqlparse 0.5.5
  - tzdata 2025.3

## 📁 Project Structure

```
ToDo/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database (created after migration)
├── templates/               # HTML templates
│   ├── home.html           # Main dashboard
│   └── edit_task.html      # Task editing page
├── todo/                    # Todo app
│   ├── models.py           # Task model definition
│   ├── views.py            # Business logic
│   ├── urls.py             # App URL patterns
│   ├── admin.py            # Admin configuration
│   └── migrations/         # Database migrations
└── todo_main/              # Project configuration
    ├── settings.py         # Django settings
    ├── urls.py            # Main URL configuration
    ├── views.py           # Home view
    └── wsgi.py            # WSGI configuration
```

## 🗄️ Database Model

### Task Model
```python
class Task(models.Model):
    task = models.CharField(max_length=250)          # Task description
    is_completed = models.BooleanField(default=False) # Completion status
    created_at = models.DateTimeField(auto_now_add=True)  # Creation timestamp
    modified_at = models.DateTimeField(auto_now=True)     # Last update timestamp
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/SiddhuBlaze3050/ToDo-app-Django.git
cd ToDo-app-Django
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## 📖 Usage

### Main Dashboard
- The home page displays all pending tasks in the left column
- Completed tasks are shown in the right column
- Current date is displayed at the top

### Adding a Task
1. Type your task in the input field at the bottom
2. Click the "+ Add" button
3. Task will appear in the pending tasks list

### Managing Tasks
- **Edit**: Click the pencil icon (✏️) to modify a task
- **Mark as Done**: Click the "Mark as Done" button (✓) to complete a task
- **Mark as Undone**: Click "Mark as Undone" (✗) on completed tasks to reactivate them
- **Delete**: Click the trash icon (🗑️) to permanently remove a task

## 🌐 URL Patterns

- `/` - Home page (pending and completed tasks)
- `/todo/addTask/` - Add new task
- `/todo/mark_as_done/<task_id>/` - Mark task as completed
- `/todo/mark_as_undone/<task_id>/` - Mark task as pending
- `/todo/edit_task/<task_id>/` - Edit existing task
- `/todo/delete_task/<task_id>/` - Delete task
- `/admin/` - Admin panel

## 🎨 UI Features

- Clean and modern interface with Bootstrap 5
- Responsive design that works on all devices
- Scrollable task lists for better space management
- Icon-based actions for intuitive user experience
- Color-coded buttons (Success, Danger, Primary) for different actions

## 🔧 Development

### Running Tests
```bash
python manage.py test
```

### Accessing Admin Panel
1. Create a superuser (see Step 5 in Installation)
2. Visit `http://127.0.0.1:8000/admin`
3. Login with superuser credentials
4. Manage tasks through Django admin interface

## 📝 Important Notes

- The `.gitignore` file is configured to exclude:
  - Virtual environment (`.venv/`)
  - Database file (`db.sqlite3`)
  - Python cache files (`__pycache__/`)
  - IDE configurations
- SQLite database is used for development; consider PostgreSQL/MySQL for production
- `DEBUG = True` in settings.py - change to `False` for production
- Update `SECRET_KEY` before deploying to production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**SiddhuBlaze3050**
- GitHub: [@SiddhuBlaze3050](https://github.com/SiddhuBlaze3050)

## 🙏 Acknowledgments

- Django Framework
- Bootstrap Team
- Font Awesome Icons

---

**Note**: This is a demonstration project for learning Django web development. Feel free to use it as a starting point for your own projects!
