from kafka.admin import KafkaAdminClient, ConfigResource, ConfigResourceType
# Kafka broker details
bootstrap_servers = "localhost:9092"  # Update this with your Kafka broker address

# Initialize Kafka Admin Client
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Define topic name and new retention settings
topic_name = "my_topic"
new_retention_ms = "604800000"  # Set retention to 7 days (in milliseconds)

# Create ConfigResource object for the topic
config_resource = ConfigResource(ConfigResourceType.TOPIC, topic_name)

# Update retention time
try:
    admin_client.alter_configs({config_resource: {"retention.ms": new_retention_ms}})
    print(f"Retention period for topic '{topic_name}' updated to {new_retention_ms} ms!")
except Exception as e:
    print(f"Error updating retention period: {e}")
