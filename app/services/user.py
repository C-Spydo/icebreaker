from app.helpers import add_record_to_database
from app.models.user import User
from app.repository.user import get_user_by_email


# def sign_in(email: str):
    # user = get_user_by_email(email)

    # if user is None:
    #     user = User(username=username)
    #     add_record_to_database(user)

    # serialized_user = user.serialize()

    # chat_memories = serialized_user['chats']

    # for i, chat_memory in enumerate(chat_memories):
    #     if chat_memory is not None:
    #         chat_memories[i]['memory'] = chat_memory['memory'].load_memory_variables({})["history"]

    # return serialized_user