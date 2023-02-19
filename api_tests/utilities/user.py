class User:

    def __init__(self, name, email, gender, status, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    def compare(self, other, ignore_id=False):
        """
        Compares two users field by field
        :param other: other user to compare
        :param ignore_id: should 'id' fields of users be compared or ignored
        :return: True if users are equal, False - otherwise
        """
        if not isinstance(other, User):
            return False

        comparison = self.name == other.name and self.email == other.email and \
                     self.gender == other.gender and self.status == other.status  # result of comparison without id

        if not ignore_id:
            comparison = comparison and (self.id == other.id)

        return comparison

    def get_json(self):
        """
        Returns user in a view of json dictionary that could be passed to request body. 'Id' field is not included
        :return: Json dictionary view of user object without id
        """
        json = {"name": self.name,
                "email": self.email,
                "gender": self.gender,
                "status": self.status}
        return json

    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\nemail: {self.email}\ngender: {self.gender}\nstatus: {self.status}"





