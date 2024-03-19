# PostgreSQL Database Interaction with Python Application

This repository contains a Python application that connects to a PostgreSQL database and performs CRUD (Create, Read, Update, Delete) operations on a `students` table.

## Setup Instructions

### 1. PostgreSQL Database Setup

#### 1.1 Installation

- Download and install PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/).


## 1.2 PostgreSQL Server Setup

To start the PostgreSQL server, follow these steps:

1. Open Command Prompt as administrator.
2. Navigate to the PostgreSQL installation directory:

    ```shell
    cd C:\Program Files\PostgreSQL\{version}\bin
    ```

3. Type the following command to start the server:

    ```shell
    pg_ctl.exe -D "../data" start 
   
    ```

4. Once the server has started, open the pgAdmin4 panel and add a server using the default credentials:

    - Username: postgres
    - Password: fast

## Python Setup

To set up Python for interacting with PostgreSQL, execute the following command:
"pip install psycopg2"

Now Execute the code and let the functions work.

Youtube link: https://youtu.be/UG7217LCBlU