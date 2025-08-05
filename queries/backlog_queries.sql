-- All tasks still in backlog
SELECT * FROM tasks
WHERE status = 'Backlog';

-- Backlog tasks by priority
SELECT priority, COUNT(*) AS task_count
FROM tasks
WHERE status = 'Backlog'
GROUP BY priority;

-- Tasks pending for more than 30 days
SELECT *
FROM tasks
WHERE status != 'Completed'
  AND DATEDIFF(CURDATE(), created_at) > 30;
