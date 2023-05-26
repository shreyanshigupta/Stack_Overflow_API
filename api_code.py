import requests
import psycopg2

# Fetch data from Stack Overflow API
def fetch_data():
    url = "https://api.stackexchange.com/"
    params = {
        "site": "stackoverflow",
        "fromdate": "start_date",
        "todate": "end_date",
        "order": "desc",
        "sort": "creation"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data['items']  # Extract relevant items from the response

# Transform and store data in PostgreSQL database
def store_data(data):
    conn = psycopg2.connect(
        database="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )

    cursor = conn.cursor()

    for item in data:
        # Extract relevant fields from the item and perform necessary transformations
        title = item['title']
        tags = item['tags']
        # Add more fields as needed

        # Store the transformed data in the database
        insert_query = "INSERT INTO stack_overflow_data (title, tags) VALUES (%s, %s);"
        cursor.execute(insert_query, (title, tags))

    conn.commit()
    cursor.close()
    conn.close()

# Execute the process
data = fetch_data()
store_data(data)
