from matplotlib import image, pyplot as plt

class Post():
    def __init__(self, description, user):
        self.__description = description
        self.__user = user
    """
    @return: the description of the post.
    """
    def get_description(self):
        return self.__description
    """
    @return: the user that published the post.
    """
    def get_user(self):
        return self.__user

    """
    @brief: notifies the user about the received like.
    @param user2: the user that liked the post.
    """
    def like(self,user2):
        if user2.get_isOnline():
            if(self.__user.get_username() != user2.get_username()):
                print("notification to " + self.__user.get_username() + ": " + user2.get_username() + " liked your post")
                self.get_user().notify(user2.get_username() + " liked your post")
    """
    @brief: notifies the user about the received comment.
    @param user2: the user that commented the post.
    @param theComment: the comment he wrote.
    """
    def comment(self,user2,theComment):
        if user2.get_isOnline():
            if(self.__user.get_username() != user2.get_username()):
                print("notification to " + self.__user.get_username() + ": " + user2.get_username()  + " commented on your post: " + theComment)
                self.get_user().notify(user2.get_username()  + " commented on your post")

class TextPost(Post):
    def __init__(self, description, user):
        super().__init__(description, user)
    """
    @brief: prints the user that published the Text Post and the Text Post description.
    """
    def __repr__(self):
        return self.get_user().get_username()  + " published a post:\n" + '"' + self.get_description() + '"' + "\n"
class ImagePost(Post):
    def __init__(self, description, user):
        super().__init__(description, user)

    """
    @brief: prints the user that published the Image Post + posted a picture.
    """
    def __repr__(self):
        return self.get_user().get_username() + " posted a picture" + "\n"

    """
    @brief: display the image of the post on the screen.
    """
    def display(self):
        image1 = image.imread(self.get_description())
        plt.imshow(image1)
        plt.title('Loaded Image')
        print("Shows picture")
        plt.axis("off")
        plt.show()
        ...
class SalePost(Post):
    def __init__(self, description, user, price, location):
        super().__init__(description,user)
        self.__price = price
        self.__location = location
        self.__available = True

    """
    @brief: prints the user that published the Sale Post + the description + the price + the location..
    """
    def __repr__(self):
        if self.__available:
            return (self.get_user().get_username() + " posted a product for sale:\n"
            + "For sale! " + self.get_description() + ", price: " + str(self.__price) + ", pickup from: " + self.__location +"\n")
        return (self.get_user().get_username() + " posted a product for sale:\n"
            + "Sold! " + self.get_description() + ", price: " + str(self.__price) + ", pickup from: " + self.__location + "\n")
    """
    @brief: updates the price to the price with the discount
    @param theDiscount: the percentage discount that needs to be calculated.
    @param password: the password of the user that published the Sale Post.
    """
    def discount(self,theDiscount, password):
        if password == self.get_user().get_password() and self.get_user().get_isOnline():
            self.__price *= ((100-theDiscount)/100)
            print("Discount on " + self.get_user().get_username() + " product! the new price is: " + str(self.__price))
    """
    @brief: updates the Sale Post to sold.
    @param password: the password of the user that published the Sale Post.
    """
    def sold(self, password):
        if password == self.get_user().get_password() and self.get_user().get_isOnline():
            self.__available = False
            print(self.get_user().get_username() + "'s product is sold")