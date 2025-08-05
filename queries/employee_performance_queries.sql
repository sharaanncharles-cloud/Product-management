-- Number of tasks completed by each employee
SELECT assigned_to, COUNT(*) AS completed_tasks
FROM tasks
WHERE status = 'Completed'
GROUP BY assigned_to;

-- Average time taken to complete tasks
SELECT assigned_to, AVG(DATEDIFF(completed_at, start_date)) AS avg_completion_days
FROM tasks
WHERE status = 'Completed'
GROUP BY assigned_to;

-- Employees with most pending tasks
SELECT assigned_to, COUNT(*) AS pending_tasks
FROM tasks
WHERE status != 'Completed'
GROUP BY assigned_to
ORDER BY pending_tasks DESC;
