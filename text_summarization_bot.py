import socket
from urllib.parse import unquote_plus  # Better than unquote: handles '+' as space

def summarize_text(text):
    # Simple summarization: first sentence or 50 characters max
    if "." in text:
        return text.split('.')[0] + '.'
    elif len(text) > 50:
        return text[:50] + '...'
    else:
        return text

HOST = '127.0.0.1'
PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[Server Running] Visit: http://{HOST}:{PORT}")

while True:
    client_conn, client_addr = server_socket.accept()
    request = client_conn.recv(2048).decode()
    print("[Request Received]:\n", request)

    request_line = request.splitlines()[0]
    method, path, _ = request_line.split()

    original_text = ""
    summary = ""

    if method == "POST":
        body = request.split("\r\n\r\n", 1)[1]
        body = unquote_plus(body)  # Replaces %XX and '+' to space
        if body.startswith("text="):
            original_text = body.replace("text=", "")
            summary = summarize_text(original_text)

    html = f"""
    <html>
        <head><title>Text Summarizer</title></head>
        <body>
            <h1>Text Summarizer</h1>
            <form method="POST" action="/">
                <textarea name="text" rows="6" cols="60" placeholder="Paste your text here..."></textarea><br>
                <button type="submit">Summarize</button>
            </form>
            <hr>
            <h2>Original Text:</h2>
            <p>{original_text}</p>
            <h2>Summary:</h2>
            <p>{summary}</p>
        </body>
    </html>
    """

    response = f"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html)}

{html}
"""
    client_conn.sendall(response.encode())
    client_conn.close()