# DSERV : Authoritative DNS Name Server
### Written in Python (nearly) from scratch

dserv is a custom Authoritative DNS Name Server built with Python that handles DNS queries and retrieves DNS records from a MongoDB database. This project aims to provide a flexible and efficient way to manage DNS zones and records.

Based on [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035) Internet Standard: **DOMAIN NAMES - IMPLEMENTATION AND SPECIFICATION**

## Tech Used
<img src="https://skillicons.dev/icons?i=py,mongodb" />

## Features

- **DNS over UDP**: Handles DNS requests over UDP.
- **Threaded Server**: Utilizes a threaded UDP server for handling multiple requests concurrently.
- **MongoDB Integration**: Retrieves DNS records from a MongoDB database, allowing dynamic and scalable DNS management.
- **Supports Multiple Record Types**: A, AAAA, MX, CNAME, NS, DNAME, PTR, and TXT record types.

## Architecture
![image](https://github.com/user-attachments/assets/e5b83444-d617-4b3c-988c-29bcdd772330)

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/ahmfaiz/dserv.git
    cd dserv
    ```

2. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

3. **Setup MongoDB**

    Ensure MongoDB is installed and running. Create a database named `dns_database` and a collection named `dns_zones`.

## Usage

1. **Add DNS Zones and Records**

    Insert DNS zones and records into the MongoDB collection `dns_zones`. An example document structure:

    ```json
    {
      "zone_name": "example.com",
      "records": [
        {
          "name": "@",
          "type": "A",
          "value": "192.0.2.1",
          "ttl": 300
        },
        {
          "name": "www",
          "type": "CNAME",
          "value": "example.com.",
          "ttl": 300
        }
      ]
    }
    ```

2. **Start the DNS Server**

    ```sh
    python server.py
    ```

    The server will start and listen on port `9876` for DNS requests.

## Code Overview

### `dserv.py`

The main script for the DNS server:

- **`DNShandler`**: Handles incoming DNS requests.
- **`convert_answer`**: Converts the database record value to the appropriate DNS record type.
- **`main`**: Starts the threaded UDP server on the specified host and port.

### `db_handler.py`

Handles database interactions:

- **`load_zone`**: Loads the best-matched zone for a given domain name from the MongoDB collection.
- **`db_lookup`**: Looks up the DNS record in the database and returns the record value and TTL.

## Example

Run the server and query it using `dig`:

```sh
dig @localhost -p 9876 example.com A
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you wanna add or fix anything.

## License

This project is licensed under the MIT License.

## Contact

Contact me at [faiz@ahmed.slmail.me](mailto:faiz@ahmed.slmail.me) if you wanna ask or say anything :)
