# import motor.motor_asyncio


# # MONGO_DETAILS = "mongodb://localhost:27017"
# MONGO_DETAILS ="mongodb+srv://adarsh:Happy@new1-smr9o.mongodb.net/test?authSource=admin&replicaSet=new1-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# print(client)

# database = client.students

# student_collection = database.get_collection("students_collection")
# # helpers


# def student_helper(student) -> dict:
#     return {
#         "id": str(student["_id"]),
#         "fullname": student["fullname"],
#         "email": student["email"],
#         "course_of_study": student["course_of_study"],
#         "year": student["year"],
#         "GPA": student["gpa"],
#     }