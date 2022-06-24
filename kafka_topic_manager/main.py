from genericpath import exists
from confluent_kafka.admin import AdminClient, NewTopic
from utils import ensure_config_is_valid
from typing import List

class KafkaTopicMgr:
    def __init__(self, conf: dict):
        ensure_config_is_valid(conf)
        self.conf = conf
        # create the admin client
        self.kafka_admin = AdminClient(self.conf)

    def check_if_single_topic_already_exists(self, topic_name: str) -> True:
        # retrieve already existing topic names
        existing_topics = self.kafka_admin.list_topics()
        return existing_topics.topics.get(topic_name) is None

    def create_topic(self, topic_names: list, num_partitions: int=1, num_replicas:int=1):
        # check if topic exists
        # if they dont exist, create
        topics_to_create = []
        for topic_name in topic_names:
            exists_flag = self.check_if_single_topic_already_exists(topic_name=topic_name)
            if exists_flag == False:
                new_topic = NewTopic(topic_name, num_partitions, num_replicas)
                topics_to_create.append(new_topic)
        self.kafka_admin.create_topics(topics_to_create)
        

    def delete_topic(self, topic_names: list):
        # check if topic exits
        # if the do, delete
        topics_to_delete = []
        for topic_name in topic_names:
            exists_flag = self.check_if_single_topic_already_exists(topic_name=topic_name)
            if exists_flag == True:
                topics_to_delete.append(topic_name)
        futures = self.kafka_admin.delete_topics(topics_to_delete, operation_timeout=30)

        # Wait for operation to finish.
        for topic, future in futures.items():
            try:
                future.result()  # The result itself is None
                print("Topic {} deleted".format(topic))
            except Exception as e:
                print("Failed to delete topic {}: {}".format(topic, e))