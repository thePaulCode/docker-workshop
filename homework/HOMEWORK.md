Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

```
docker run  -it ubuntu

docker run -it --entrypoint=bash  -v $(pwd)/homework:/app/homework python:3.13.11-slim

pip --version
pip 25.3
```

Question 2. Understanding Docker networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

```
db:5432
```

Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

```
SELECT 
	count(*) AS "total_trips"
FROM
	green_trip_data g
WHERE 
	g.trip_distance <= 1 
	AND g.lpep_pickup_datetime >= '2025-11-01' 
	AND g.lpep_pickup_datetime < '2025-12-01';

Data Output:
total_trips = 8007	
```
Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.

2025-11-14 |
2025-11-20 |
2025-11-23 |
2025-11-25
```
WITH daily_max AS (SELECT 
	CAST(lpep_pickup_datetime AS DATE) AS pickup_day,
	MAX(trip_distance) AS max_distance
FROM
	green_trip_data
WHERE trip_distance < 100
GROUP BY CAST(lpep_pickup_datetime AS DATE)
)

SELECT
	pickup_day, 
	max_distance
FROM daily_max
ORDER BY max_distance DESC
LIMIT 1;

Data Output:
"2025-11-14"	88.03
```

Question 5. Biggest pickup zone
Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

East Harlem North |
East Harlem South |
Morningside Heights |
Forest Hills

```
WITH zones_total_amount AS (
	SELECT 
		CAST(lpep_pickup_datetime AS DATE) AS trip_day,
		"Zone",
		SUM(total_amount) AS sum_total_amount
	FROM
		green_trip_data g
	INNER JOIN taxi_zones zpu
	ON g."PULocationID" =  zpu."LocationID"
	WHERE 
	lpep_pickup_datetime >= '2025-11-18' AND
	lpep_pickup_datetime < '2025-11-19' 
	GROUP BY 1,2
)
SELECT "Zone"
FROM
	zones_total_amount z
ORDER BY z.sum_total_amount DESC
LIMIT 1;

Data Output:
"East Harlem North"
```

Question 6. Largest tip
For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's tip , not trip. We need the name of the zone, not the ID.

JFK Airport |
Yorkville West |
East Harlem North |
LaGuardia Airport
```
SELECT 	zdo."Zone",
		g.tip_amount 
FROM
	green_trip_data g
INNER JOIN taxi_zones zpu
ON g."PULocationID" =  zpu."LocationID"
INNER JOIN taxi_zones zdo
ON g."DOLocationID" =  zdo."LocationID"
WHERE 
	g.lpep_pickup_datetime >= '2025-11-01' AND
	g.lpep_pickup_datetime < '2025-12-01' AND
	zpu."Zone" = 'East Harlem North'
ORDER BY g.tip_amount DESC
LIMIT 1;

Data Output:
Yorkville West

```