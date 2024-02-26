from User import User


class SocialNetwork:
    __network = None
    __users = []

    @staticmethod
    def __new__(cls, name):
        if not cls.__network:
            cls.__network = super(SocialNetwork, cls).__new__(cls)
            cls.__network.name = name
            print("The social network " + cls.__network.name + " was created!")
            
        return cls.__network
        # Example usage:
    """
    @brief: prints the social network and its users.
    """
    def __repr__(self):
        st = self.__network.name + " social network:\n"
        for user in self.__users:
            st += str(user) + "\n"
        return str(st)
    """
    @brief: sign up a user to the social network.
    @param name: the name of the user.
    @param password: the password of the user.
    @return: the user.
    """
    def sign_up(self, name, password):
        available = True
        for username in self.__users:
            if name == username:
                print("the name is already taken")
                available = False
                break
        if available:
            if len(password) < 4 or len(password) > 8:
                print("the password isn't valid, password need to be between 4-8 characters")
            else:
                user = User(name, password)
                self.__users.append(user)
                user.set_online_status(True)
                return user

    """
    @brief: log in the user to the social network.
    @param name: the name of the user.
    @param password: the password of the user.
    @return: the user.
    """
    def log_in(self, name, password):
        for i in range(len(self.__users)):
            if self.__users[i].get_username() == name and self.__users[i].get_password() == password:
                user = User(name, password)
                user.set_online_status(True)
                print(name + " connected")
                return user
    """
    @brief: log out the user from the social network.
    @param name: the name of the user.
    """
    def log_out(self, name):
        for i in range(len(self.__users)):
            if self.__users[i].get_username() == name:
                user = self.__users[i]
                user.set_online_status(False)
                print(user.get_username() + " disconnected")