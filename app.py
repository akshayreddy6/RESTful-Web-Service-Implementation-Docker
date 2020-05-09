from flask import Flask, jsonify

app = Flask(__name__, static_url_path='')




def filter_by_id(id):
    users = [
        {
            'id': '1',
            'name': 'customer 1',
            'friends': ['2', '3'],
        },
        {
            'id': '2',
            'name': 'customer 2',
            'friends': ['1'],
        },
        {
            'id': '3',
            'name': 'customer 3',
            'friends': ['1'],
        }
    ]

    res = list(filter(lambda user: str(user['id']) == id, users))
    print(res)
    return res


@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {
            'id': '1',
            'name': 'customer 1',
            'friends': ['2', '3'],
        },
        {
            'id': '2',
            'name': 'customer 2',
            'friends': ['1'],
        },
        {
            'id': '3',
            'name': 'customer 3',
            'friends': ['1'],
        }
    ]
    return jsonify(users)


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return jsonify(filter_by_id(id))


@app.route('/users/<id>/friends', methods=['GET'])
def get_user_friends(id):
    usr = filter_by_id(id)
    res = []
    for fr in usr[0]['friends']:
        res.append(filter_by_id(fr)[0])
    return jsonify(res)


if __name__ == '__main__':
    print("hello")
    app.run(debug=True,host='0.0.0.0')
