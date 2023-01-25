
CREATE TABLE department
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  location VARCHAR(255)
);

CREATE TABLE employee 
(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  salary INT,
  dept_id INT,
  FOREIGN KEY(dept_id) REFERENCES department(id)
);

INSERT INTO department(name, location) VALUES ('Executive', 'Sydney');
INSERT INTO department(name, location) VALUES ('Production', 'Sydney');
INSERT INTO department(name, location) VALUES ('Resources', 'Cape Town');
INSERT INTO department(name, location) VALUES ('Technical', 'Texas');
INSERT INTO department(name, location) VALUES ('Management', 'Paris');

INSERT INTO employee(name, salary, dept_id) VALUES ('Candice', 4685, 1);
INSERT INTO employee(name, salary, dept_id) VALUES ('Julia', 4685, 2);
INSERT INTO employee(name, salary, dept_id) VALUES ('Bob', 4685, 4);
INSERT INTO employee(name, salary, dept_id) VALUES ('Scarlet', 4685, 1);
INSERT INTO employee(name, salary, dept_id) VALUES ('Ileana', 4685, 4);


SELECT department.name AS department_name,
       IFNULL(COUNT(employee.dept_id), 0) AS employee_count
FROM department
LEFT JOIN employee
ON department.id = employee.dept_id
GROUP BY department.id
ORDER BY employee_count DESC, department_name;
