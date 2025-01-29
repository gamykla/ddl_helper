CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    salary DECIMAL(10, 2) DEFAULT 0.00,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE keys (
    key VARCHAR(100),
    value VARCHAR(100);
);
