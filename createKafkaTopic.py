from kafka.admin import KafkaAdminClient, NewTopic

bootstrap_servers = "localhost:9092"  # Update this with your Kafka broker address

# Initialize Kafka Admin Client
admin_client = KafkaAdminClient(
    bootstrap_servers=bootstrap_servers
)

# Define multiple topics with their configurations
topics_to_create = [
    NewTopic(name="topic_one", num_partitions=3, replication_factor=1),
    NewTopic(name="topic_two", num_partitions=2, replication_factor=1),
    NewTopic(name="topic_three", num_partitions=4, replication_factor=2)
]

# Create multiple topics
try:
    admin_client.create_topics(topics_to_create)
    print("Topics created successfully!")
except Exception as e:
    print(f"Error creating topics: {e}")
