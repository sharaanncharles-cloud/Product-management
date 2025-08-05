-- Create a table for product managers
CREATE TABLE product_managers (
    pm_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50)
);

-- Create a table for product features
CREATE TABLE features (
    feature_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    description TEXT,
    status VARCHAR(50), -- e.g., 'Backlog', 'In Progress', 'Completed'
    pm_id INT,
    FOREIGN KEY (pm_id) REFERENCES product_managers(pm_id)
);

-- Create a table for sprints
CREATE TABLE sprints (
    sprint_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

-- Create a linking table for sprint-feature assignments
CREATE TABLE sprint_features (
    sprint_id INT,
    feature_id INT,
    PRIMARY KEY (sprint_id, feature_id),
    FOREIGN KEY (sprint_id) REFERENCES sprints(sprint_id),
    FOREIGN KEY (feature_id) REFERENCES features(feature_id)
);
