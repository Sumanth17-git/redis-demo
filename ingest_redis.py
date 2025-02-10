import redis
import json
import random
import time

# Connect to Redis (Using the ClusterIP service inside Kubernetes)
redis_host = "redis-service"  # Update with your Redis service name
redis_port = 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)

# Define 10 random categories
CATEGORIES = ["Tech", "Sports", "Music", "Movies", "Books", "Fashion", "Food", "Travel", "Fitness", "Gaming"]

# Insert 100K user data
NUM_USERS = 100000

print("🚀 Starting data ingestion into Redis...")

for i in range(1, NUM_USERS + 1):
    user_id = f"user_{i}"
    recommendations = random.sample(CATEGORIES, k=random.randint(1, 5))  # Assign 1-5 random categories

    # Save to Redis
    redis_client.set(f"user:{user_id}:recommendations", json.dumps(recommendations))

    if i % 10000 == 0:
        print(f"✅ Inserted {i} users...")

print("🎉 Data ingestion completed successfully!")