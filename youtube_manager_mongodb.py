from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://<username>:<password>@cluster0.1muoh.mongodb.net/")

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)


def add_video(name, time):
    video_collection.insert_one({"name":  name, "time": time})


def list_videos():
    for video in video_collection.find():
        print(
            f"ID: {video['_id']}, Name: {video['name']}, Time:{video['time']}")


def update_video(video_id, new_name, new_time):
    try:
        oid = ObjectId(video_id)
    except Exception as e:
        print(f"Invalid video id format: {e}")
        return

    video_collection.update_one({'_id': oid},
                                {"$set": {"name": new_name, "time": new_time}})

    print("Successfully updated video ", oid)


def delete_video(video_id):
    try:
        oid = ObjectId(video_id)
    except Exception as e:
        print("Invalid video id format: {e}")
        return
    video_collection.delete_one({"_id": video_id})
    print("Successfully deleted video", oid)


def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video id to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video id to be deleted: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
