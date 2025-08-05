-- Insert sample product managers
INSERT INTO product_managers (name, email, department)
VALUES 
('Alice Johnson', 'alice.johnson@example.com', 'AI Products'),
('Bob Smith', 'bob.smith@example.com', 'Mobile Apps');

-- Insert sample features
INSERT INTO features (title, description, status, pm_id)
VALUES 
('User Login System', 'Allow users to register and log in', 'Completed', 1),
('Dark Mode', 'Implement dark mode for UI', 'In Progress', 2);

-- Insert sample sprints
INSERT INTO sprints (name, start_date, end_date)
VALUES 
('Sprint 1', '2025-08-01', '2025-08-15'),
('Sprint 2', '2025-08-16', '2025-08-30');

-- Link features to sprints
INSERT INTO sprint_features (sprint_id, feature_id)
VALUES 
(1, 1),
(2, 2);
