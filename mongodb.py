# from pymongo import MongoClient
# from setting import MONGO_DB
# from setting import MONGODB_LINK
#
# mdb = MongoClient(MONGODB_LINK)[MONGO_DB] # переменная для работы с БД
#
# def serch_or_save_user(mdb, effective_user, message):
#     user = mdb.users.find_one({"user_id":effective_user.id}) # поиск  в коллекции users по users_id
#     if not user: # если таковог нет создадми словарь с данными
#         user = {
#             "user_id":effective_user.id,
#             "first_name":effective_user.first_name,
#             "last_name":effective_user.last_name,
#             "chat_id":message.chat.id
#         }
#         mdb.users.insert_one(user) # охраняем в коллекции users
#     return user
#
# # сохраняем - изменяем результаты анкеты и возвращаем результат
# def save_user_anketa(mdb, user, user_data):
#     mdb.users.update_one(
#         {'_id': user['_id']},
#         {'$set' : {'anketa': {'name': user_data['name'],
#                               'age': user_data['age'],
#                               'evaluation': user_data['evaluation'],
#                               'comment': user_data['comment']
#                               }
#                    }
#          }
#     )
#     return user

