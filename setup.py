from setuptools import setup, find_packages

setup(
  name = 'kafka_topic_manager',
  version = '0.0.1',
  license='MIT',
  description = 'A simple wrapper for confluent_kafka admin functionalities for managing kafka topics',
  long_description_content_type = 'text/markdown',
  author = 'Nachiket Makwana',
  author_email = 'nachimak28@gmail.com',
  url = 'https://github.com/Nachimak28/kafka_topic_manager',
  keywords = [
    'data streaming',
    'data engineering',
    'event bus',
    'queue',
    'kafka',
    'distributed computing'
  ],
  install_requires=[
    'confluent-kafka>=1.4.2',
  ],
  classifiers=[
    'DEVELOPMENT STATUS :: 3 - ALPHA',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Data Engineering',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)