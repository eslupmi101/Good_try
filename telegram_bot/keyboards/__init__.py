if __name__ != '__main__':
    from keyboards.user_kb import user_kb
    from keyboards.lord_kb import lord_kb
    from keyboards.agent_kb import agent_kb, agent_accept_kb
    def get_kb(user_type):
        if user_type == 'User':
            return user_kb
        elif user_type == 'Agent':
            return agent_kb
        elif user_type == 'Lord':
            return lord_kb
        elif user_type == 'Accept':
            return agent_accept_kb
        else:
            return None

else:
    from user_kb import user_kb
    from lord_kb import lord_kb
    from agent_kb import user_kb