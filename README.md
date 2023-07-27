## Simple Web Server

<p>This project serves as a basic web server built using Python that can handle HTTP requests and responses. It provides functionality to serve static files, generate dynamic pages, and run external CGI programs. The server is designed to be extensible, allowing developers to add new features and custom handling for different types of requests.</p>

## Features
<ol>
<li>Serving Static Files: The web server can serve static files (HTML, CSS, JavaScript, images, etc.) from the current directory or its subdirectories.</li>

<li>Dynamic Page Generation: It can generate dynamic HTML pages in response to certain requests.</li>

<li>CGI Support: The server supports running external CGI programs, allowing developers to add custom functionality by writing separate Python scripts or other executable programs.</li>

<li>Directory Listing: If a directory doesn't have an index.html file, the server displays a listing of the directory's contents.</li>

<li>Error Handling: The server provides error pages for different types of errors (e.g., file not found) and returns appropriate status codes.
</ol>

Original from <a href="https://aosabook.org/en/500L/a-simple-web-server.html">500 lines or less</a>
