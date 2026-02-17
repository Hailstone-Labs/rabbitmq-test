# RabbitMQ Examples

This repository contains Python scripts that demonstrate various messaging patterns using RabbitMQ.

## Prerequisites

*   Python 3.13+
*   RabbitMQ server running

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/rabbitmq-test.git
    cd rabbitmq-test
    ```
2.  **Install dependencies:**
    ```bash
    pip install pika
    ```

## Examples

### 1. Hello World

This example demonstrates a simple producer-consumer pattern.

*   **Start the consumer:**
    ```bash
    python receive.py
    ```
*   **Send a message:**
    ```bash
    python send.py
    ```
    You should see the message "Hello World!" printed by the `receive.py` script.

### 2. Work Queues

This example demonstrates a work queue where a producer sends tasks to a queue and multiple workers can process them.

*   **Start one or more workers:**
    ```bash
    python worker.py
    ```
*   **Send a task:**
    ```bash
    python new_task.py "This is a task..."
    ```
    The `worker.py` script will receive the message and simulate work by sleeping for a few seconds. You can run multiple `worker.py` instances to see how they share the workload.
