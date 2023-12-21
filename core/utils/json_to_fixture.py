import json


with open('creators.json') as creators_file:
    parsed_creators = json.load(creators_file)

    users = [
        {"model": "auth.user", "pk": 1, "fields": {
            "username": "admin", "password": "admin"
        }}
    ]
    creators = []
    content = []

    for i, k in enumerate(parsed_creators):
        id = i
        users.append({
            "model": "auth.user", "pk": id+1, "fields": {
                "username": k["username"]
            }
        })
        # creators.append({"model": "creators.creator", "pk": id+1})
        # content.append({"model": "creators.content", })

    print(creators)
    print(content)
    print(users)
