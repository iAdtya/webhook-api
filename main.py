from flask import Flask
from flask import request, json
import logging
from config import client

# from schema import YourSchema

app = Flask(__name__)
app.logger.setLevel(logging.INFO)  


def create_app():
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return app


app = create_app()


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/receiver", methods=["POST"])
def receiver():
    if request.headers["Content-Type"] == "application/json":
        data = request.get_json()
        github_event = request.headers.get("X-Github-Event")

        if github_event == "push":
            author = data["head_commit"]["author"]["name"]
            author_id = data["head_commit"]["id"]
            to_branch = data["ref"].split("/")[-1]
            timestamp = data["head_commit"]["timestamp"]
            print(f"{author} pushed to {to_branch} on {timestamp}")
            data = {
                "request_id": author_id,  
                "author": author,
                "action": "push",
                "from_branch": "",
                "to_branch": to_branch,
                "timestamp": timestamp,
            }
            send_data(data)
            return "Success", 200

        elif github_event == "pull_request":
            action = data["action"]
            if action == "opened" or action == "synchronize":
                author = data["pull_request"]["user"]["login"]
                from_branch = data["pull_request"]["head"]["ref"]
                to_branch = data["pull_request"]["base"]["ref"]
                timestamp = data["pull_request"]["updated_at"]
                request_id = data["pull_request"]["id"]
                message = f"{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}"
                print(message)
                data = {
                    "request_id": request_id,  
                    "author": author,
                    "action": action,
                    "from_branch": from_branch,
                    "to_branch": to_branch,
                    "timestamp": timestamp,
                }
                send_data(data)

                return "Success", 200

            elif action == "closed":
                pull_request = data["pull_request"]
                if pull_request["merged"]:
                    author = pull_request["user"]["login"]
                    from_branch = pull_request["head"]["ref"]
                    to_branch = pull_request["base"]["ref"]
                    timestamp = pull_request["merged_at"]
                    request_id = pull_request["id"]
                    message = f"{author} merged branch {from_branch} to {to_branch} on {timestamp}"
                    print(message)
                    data = {
                        "request_id": request_id,  
                        "author": author,
                        "action": action,
                        "from_branch": from_branch,
                        "to_branch": to_branch,
                        "timestamp": timestamp,
                    }
                    send_data(data)
                    return "Success", 200

        return "Unsupported event", 200


def send_data(data: dict):
    try:
        db = client.test_database
        collection = db.stax  
        collection.insert_one(data)
        print("Data inserted successfully")
    except Exception as e:
        print(f"Error in inserting the data: {e}")


if __name__ == "__main__":
    app.run(debug=True)
