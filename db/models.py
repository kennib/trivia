# The models for Trivia

import sqlite3
import hasher

class Model:
    def __init__():
        pass

    @classmethod
    def _table_name(cls):
        return cls.__name__.lower() + 's'

    @classmethod
    def find(cls, **kwargs):
        table_name = cls._table_name()
        query = 'SELECT * FROM {0} WHERE'.format(cls._table_name())

        for key in kwargs:
            query += ' ' + key + ' = ?'
        values = tuple(kwargs.values())

        cur = conn.cursor()
        cur.execute(query, values)
        result = cur.fetchone()
        return cls(**result)


class User(Model):
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email

    @classmethod
    def check_login(cls, username, password):
        cur = conn.cursor()
        cur.execute('SELECT username, password_hash FROM users WHERE username = ?', (username,))
        result = cur.fetchone()
        return hasher.hash(password) == result['password_hash']

    @classmethod
    def find(cls, **kwargs):
        query = 'SELECT user_id, username, email FROM users WHERE'
        for key in kwargs:
            query += ' ' + key + ' = ?'
        values = tuple(kwargs.values())

        cur = conn.cursor()
        cur.execute(query, values)
        result = cur.fetchone()
        return cls(**result)

    @classmethod
    def create(cls, username, password, email):
        raise NotImplementedError()
        return cls(0, username, hash_password(password), email)

    @classmethod
    def delete_by_id(cls, user_id):
        raise NotImplementedError()
        return True

    @classmethod
    def delete_by_username(cls, username):
        raise NotImplementedError()
        return True

    def set_email(self, new_email):
        cur = conn.cursor()
        cur.execute('UPDATE users SET email = ? WHERE uid = ?', (new_email, self.id))
        self.email = self.new_email
        cur.commit()

class TriviaQuestion(Model):
    def __init__(self, question_id, question, num_answered, num_correct, category):
        self.id = question_id
        self.question = question
        self.num_answered = num_answered
        self.num_correct = num_correct
        self.category = category

    @classmethod
    def create(cls, question, category):
        raise NotImplementedError
        # num_answered = 0
        # num_correct = 0
        ...
        return cls(qid, question, 0, 0, category)

    def flag(self):
        return Flag.create(self.id)


class Category(Model):
    def __init__(self, category_id, name):
        self.id = category_id
        self.name = name

    @classmethod
    def _table_name(cls):
        return 'categories'

    @classmethod
    def create(cls, name):
        raise NotImplementedError
        ...
        return cls(cid, name)


class Flag(Model):
    def __init__(self, flag_id, question_id):
        self.id = flag_id
        self.question_id = question_id

    @classmethod
    def create(cls, question_id):
        raise NotImplementedError()


class Answer(Model):
    def __init__(self, answer_id, question_id, correct, text):
        self.id = answer_id
        self.question_id = question_id
        self.correct = correct
        self.text = text

    @classmethod
    def create(cls, answer_id, question_id, correct, text):
        raise NotImplementedError()

    @classmethod
    def delete_by_id(cls, answer_id):
        raise NotImplementedError()


class Score(Model):
    def __init__(self, user_id, category_id, num_answered, num_correct):
        self.user_id = user_id
        self.category_id = category_id
        self.num_answered = num_answered
        self.num_correct = num_correct

    @classmethod
    def create(cls, user_id, category_id):
        raise NotImplementedError()


conn = sqlite3.connect('db/trivia.db')
