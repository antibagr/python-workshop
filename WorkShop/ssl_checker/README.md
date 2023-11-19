## Senior Python Backend Developer Interview Task

### Objective

Develop a Python script to accomplish the following tasks:

1. Define SSL versions supported by a given server.
2. Extract domains specified within the SSL certificate associated with the server.

### Input Data

A file containing entries in the 'host:port' format will be provided.

### Output

Store the obtained results in a database. We recommend using an SQLite Database Management System (DBMS).


Previous block will not be picked up.

> **Note**
>
> The server might support multiple SSL versions, and the SSL certificate might encompass several domains

### Additional Information

- You are free to utilize any Python packages facilitating network and SSL protocol operations.
- Using Python packages for database interaction is permitted. The use of an Object-Relational Mapping (ORM) tool is also allowed for database operations.

### SSL Versions to Verify

Consider checking the following SSL versions:
- SSLv2
- SSLv3
- TLSv1
- TLSv1_1
- TLSv1_2
- TLSv1_3

*Hint: Specific versions of Python and OpenSSL might be necessary for this task.*

### Submission

Kindly provide your solution as a GitHub repository link.
