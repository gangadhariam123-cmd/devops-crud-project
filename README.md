# DevOps CRUD Project

A Python Flask-based CRUD REST API integrated with a MySQL database.

## Technologies Used
- Python 3
- Flask
- MySQL
- MySQL Connector
- Git
- GitHub

## Project Features
- Create employee records
- Retrieve employee records
- Update employee information
- Delete employee records
- REST API endpoints

## Project Structure
```text
devops-crud-project/
├── app.py
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/gangadhariam123-cmd/devops-crud-project.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure MySQL
Create the `devops_crud` database in MySQL.

Set your database password as an environment variable:

```powershell
$env:DB_PASSWORD="your_mysql_password"
```

### 4. Run the application
```bash
python app.py
```

The Flask application runs locally at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Home |
| GET | /health | Health check |
| GET | /employees | Retrieve employees |

## Author
Gangadhar

## License
This project is created for learning and educational purposes.
