import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field can not be left blank.'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field can not be left blank.'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'This username already exists.'}, 400

        # conn = sqlite3.connect("data.db")
        # cur = conn.cursor()
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"   # NULL due to autoincrementing id field
        # cur.execute(query, (data['username'], data['password']))
        # conn.commit()
        # conn.close()

        user = UserModel(**data)   # UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
