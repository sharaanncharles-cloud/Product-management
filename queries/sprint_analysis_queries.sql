-- Total tasks per sprint
SELECT sprint_id, COUNT(*) AS total_tasks
FROM tasks
GROUP BY sprint_id;

-- Completed vs pending tasks per sprint
SELECT sprint_id,
       SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed_tasks,
       SUM(CASE WHEN status != 'Completed' THEN 1 ELSE 0 END) AS pending_tasks
FROM tasks
GROUP BY sprint_id;

-- Average sprint completion time
SELECT AVG(DATEDIFF(end_date, start_date)) AS avg_sprint_duration
FROM sprints;
