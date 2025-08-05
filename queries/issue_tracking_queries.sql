-- Open vs closed issues
SELECT status, COUNT(*) AS issue_count
FROM issues
GROUP BY status;

-- Average resolution time
SELECT AVG(DATEDIFF(resolved_at, reported_at)) AS avg_resolution_days
FROM issues
WHERE status = 'Closed';

-- High severity unresolved issues
SELECT * FROM issues
WHERE severity = 'High'
  AND status != 'Closed';
