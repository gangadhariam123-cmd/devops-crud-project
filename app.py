
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YourPrivatePassword123",
        database="devops_crud"
    )


# HOME API
@app.route("/")
def home():
    return "Welcome to my DevOps CRUD Project!"


# HEALTH API
@app.route("/health")
def health():
    return {"status": "healthy"}


# 1. READ - Get all employees
@app.route("/employees", methods=["GET"])
def employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({"employees": data})


# 2. CREATE - Add new employee
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    required = ["name", "email", "department", "salary"]

    if not all(field in data for field in required):
        return jsonify({"error": "Missing employee fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO employees (name, email, department, salary)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (
        data["name"],
        data["email"],
        data["department"],
        data["salary"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "Employee added successfully!"
    }), 201


# 3. UPDATE - Update employee
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    required = ["name", "email", "department", "salary"]

    if not all(field in data for field in required):
        return jsonify({"error": "Missing employee fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        UPDATE employees
        SET name = %s,
            email = %s,
            department = %s,
            salary = %s
        WHERE id = %s
    """

    cursor.execute(query, (
        data["name"],
        data["email"],
        data["department"],
        data["salary"],
        id
    ))

    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({"error": "Employee not found or no changes made"}), 404

    return jsonify({
        "message": "Employee updated successfully!"
    })


# 4. DELETE - Delete employee
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id = %s",
        (id,)
    )

    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()

    if affected == 0:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({
        "message": "Employee deleted successfully!"
    })


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)
